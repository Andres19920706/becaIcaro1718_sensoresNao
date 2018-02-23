# -*- encoding: UTF-8 -*-
'''
Created on 22 feb. 2018
Tipo de sensor FSR
@info: http://doc.aldebaran.com/1-14/family/robots/fsr_robot.html
@info: http://doc.aldebaran.com/1-14/dev/python/examples/sensors/index.html#python-example-sensors
@author: Andres
nota: 
complemento de sensores: http://doc.aldebaran.com/2-4/naoqi/core/almemory-tuto.html
'''
from naoqi import ALProxy

IP = "192.168.1.39" # set your Ip address here
PORT = 9559 #49260

# ====================
# Create proxy to ALMemory
memoryProxy = ALProxy("ALMemory", IP, PORT)

# Get The Left Foot Force Sensor Values
LFsrFL = memoryProxy.getData("Device/SubDeviceList/LFoot/FSR/FrontLeft/Sensor/Value")
LFsrFR = memoryProxy.getData("Device/SubDeviceList/LFoot/FSR/FrontRight/Sensor/Value")
LFsrBL = memoryProxy.getData("Device/SubDeviceList/LFoot/FSR/RearLeft/Sensor/Value")
LFsrBR = memoryProxy.getData("Device/SubDeviceList/LFoot/FSR/RearRight/Sensor/Value")

print( "Left FSR [Kg] : %.2f %.2f %.2f %.2f" %  (LFsrFL, LFsrFR, LFsrBL, LFsrBR) )

# Get The Right Foot Force Sensor Values
RFsrFL = memoryProxy.getData("Device/SubDeviceList/RFoot/FSR/FrontLeft/Sensor/Value")
RFsrFR = memoryProxy.getData("Device/SubDeviceList/RFoot/FSR/FrontRight/Sensor/Value")
RFsrBL = memoryProxy.getData("Device/SubDeviceList/RFoot/FSR/RearLeft/Sensor/Value")
RFsrBR = memoryProxy.getData("Device/SubDeviceList/RFoot/FSR/RearRight/Sensor/Value")

print( "Right FSR [Kg] : %.2f %.2f %.2f %.2f" %  (RFsrFL, RFsrFR, RFsrBL, RFsrBR) )