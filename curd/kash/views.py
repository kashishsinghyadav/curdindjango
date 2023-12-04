from django.shortcuts import render
import io
from .models import Student
from .serializers import StudentSerial
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse,JsonResponse
from django.views.decorators.csrf import csrf_exempt
# Create your views here.
@csrf_exempt
def student_api(request):
    if request.method=='GET':
        json_data=request.body# data stored jo user ne manga hai 
        stream=io.BytesIO(json_data)# usko stream kiya
        pythondata=JSONParser().parse(stream)#
        id=pythondata.get('id',None)
        if id is not None:
            stu=Student.objects.get(id=id)
            serial=StudentSerial(stu)
            json_data=JSONRenderer().render(serial.data)
          
            return HttpResponse(json_data,content_type='application/json')
        stu=Student.objects.all()
        serial=StudentSerial(stu,many=True)
        json_data=JSONRenderer().render(serial.data)
        return HttpResponse(json_data,content_type='application/json')
    
    if request.method=='POST':
        json_data=request.body
        stream=io.BytesIO(json_data)
        pythondata=JSONParser().parse(stream)
        serial=StudentSerial(data=pythondata)
        if serial.is_valid():
            serial.save()

            res={'msg':'created'}
            json_data=JSONRenderer().render(res)
            return HttpResponse(json_data,content_type='application/json')
        json_data=JSONRenderer().render(serial.errors)
        return HttpResponse(json_data,content_type='application/json')
    
    if request.method=='PUT':
        json_data=request.body
        stream=io.BytesIO(json_data)
        pythondata=JSONParser().parse(stream)
        id=pythondata.get('id')
        stu=Student.objects.get(id=id)
        serial=StudentSerial(stu,data=pythondata,partial=True)
        if serial.is_valid():
            serial.save()
            res={'msg':'data update'}
            json_data=JSONRenderer().render(res)
            return HttpResponse(json_data,content_type='application/json')

    if request.method=='DELETE':
        json_data=request.body
        stream=io.BytesIO(json_data)
        pythondata=JSONParser().parse(stream)
        id=pythondata.get('id')
        stu=Student.objects.get(id=id)
        stu.delete()
        res={'msg':'data deleted'}
        return JsonResponse(res,safe=False)