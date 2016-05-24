from django.http import HttpResponse
from sensor.service import *
from django.shortcuts import render

# Create your views here.
def onesec(request):
    read_sensor()
    read_sensor2()
    read_sensor3()
    return HttpResponse('')
