import subprocess
from sensor.models import *
import csv

def read_sensor():
    reading1=subprocess.check_output(['sudo', 'python', '/home/pi/test_gyro/final1.py'])
    newreading1=motion_detect(reading=reading1)
    newreading1.save()
    

def read_sensor2():
    reading2=subprocess.check_output(['sudo', 'python', '/home/pi/test_gyro/final3.py'])
    newreading2=duration(reading=reading2)
    newreading2.save()

def read_sensor3():
    reading3=subprocess.check_output(['sudo', 'python', '/home/pi/test_gyro/final4.py'])
    newreading3=normalize(reading=reading3)
    newreading3.save()


    return True
