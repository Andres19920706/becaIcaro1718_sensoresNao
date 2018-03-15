# -*- encoding: UTF-8 -*-
'''
Mover la cabeza de NAO 
Created on 15 mar. 2018
@info: doc.aldebaran.com/2-1/naoqi/motion/control-joint-api.html?highlight=almotion#ALMotionProxy::setAngles__AL::ALValueCR.AL::ALValueCR.floatCR
@author: Andres
'''
import almath
import time

from naoqi import ALProxy

motionProxy = ALProxy("ALMotion", "192.168.1.39", 9559)

motionProxy.setStiffnesses("Head", 1.0)

# Example showing a single target angle for one joint
# Interpolates the head yaw to 1.0 radian in 1.0 second
names = "HeadYaw"
angleLists = 0.0#50.0*almath.TO_RAD
timeLists  = 0.5 #Tiempo que tarda en mover la cabeza
isAbsolute = True
motionProxy.angleInterpolation(names, angleLists, timeLists, isAbsolute)

time.sleep(1.0)

names = "HeadPitch"
angleLists = 0.0
timeLists  = 1
isAbsolute = True
motionProxy.angleInterpolation(names, angleLists, timeLists, isAbsolute)


time.sleep(1.0)

#o
names      = ["HeadYaw", "HeadPitch"]
angleLists = [0.5,-0.5]
timeLists  = [1.0, 1.2]
isAbsolute = True
motionProxy.angleInterpolation(names, angleLists, timeLists, isAbsolute)



"""
#-----------
names      = ["HeadYaw", "HeadPitch"]
angleLists = [30.0*almath.TO_RAD, 30.0*almath.TO_RAD]
timeLists  = [1.0, 1.2]
isAbsolute = True
motionProxy.angleInterpolation(names, angleLists, timeLists, isAbsolute)

"""