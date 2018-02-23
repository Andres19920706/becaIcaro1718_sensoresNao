# -*- coding: utf-8 -*-
'''
Created on 23 feb. 2018
http://doc.aldebaran.com/2-4/naoqi/audio/index.html
nota: http://doc.aldebaran.com/1-14/naoqi/audio/alspeechrecognition-api.html#ALSpeechRecognitionProxy::getParameter__ssCR
nota: http://doc.aldebaran.com/2-4/naoqi/audio/alsounddetection-api.html
@author: Andres
'''
from naoqi import ALProxy
import sys
IP = "192.168.1.39" # set your Ip address here
PORT = 9559 #49260

# ====================
# Create proxy to ALMemory

recog = ALProxy("ALSpeechRecognition", IP, PORT)
print "Lenguajes Avilitados: "+str(recog.getAvailableLanguages())
print "Lenguaje establecido: "+str(recog.getLanguage())
#Parámetros de reconocimeinto de voz

param = "Sensitivity"
print "Parámetro \"Sensivility\: "+str(recog.getParameter(param)) #Obtener
recog.setParameter(param,0.91) #Modificar el valor del parámetro

#Reconocer palabras solo para versioens < NAO V4 
#print "Reconocer palabra hola "+str(recog.getPhoneticTranscription("hola") )


