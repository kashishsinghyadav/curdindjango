from django.db import models

class Student(models.Model):
    name=models.CharField(max_length=10)
    st_id=models.IntegerField()
    city=models.CharField(max_length=10)

# Create your models here.
