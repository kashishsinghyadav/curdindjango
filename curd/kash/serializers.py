from rest_framework import serializers

from .models import Student

class StudentSerial(serializers.Serializer):
    name=serializers.CharField(max_length=10)
    st_id=serializers.IntegerField()
    city=serializers.CharField(max_length=10)

    def create(self,validated_data):
        return Student.objects.create(**validated_data)
    
    def update(self,instance,validated_data):
        instance.name=validated_data.get('name',instance.name)
        instance.st_id=validated_data.get('st_id',instance.st_id)
        instance.city=validated_data.get('city',instance.city)
        instance.save()
        return instance