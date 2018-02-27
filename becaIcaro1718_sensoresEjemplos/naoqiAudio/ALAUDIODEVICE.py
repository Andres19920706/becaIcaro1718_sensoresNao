# -*- encoding: UTF-8 -*-
'''
Created on 26 feb. 2018
M�dulo que trabaja con los m�todos del m�dulo ALAudioDevice

@ifo: http://doc.aldebaran.com/2-4/naoqi/audio/alaudiodevice.html
@author: Andres
'''

import logging as log
from naoqi import (ALModule, ALProxy)
import sys
import time
IP = "192.168.1.39" #"127.0.0.1
PORT = 9559 #49260
# ====================
# Create proxy to ALMemory

recog = ALProxy("ALSpeechRecognition", IP, PORT)
#recog = ALProxy("ALSoundDetection", IP, PORT)
print "Lenguajes Avilitados: "+str(recog.getAvailableLanguages())
print "Lenguaje establecido: "+str(recog.getLanguage())
#Par�metros de reconocimeinto de voz

# ==================== Inicialziaci�n de los m�dulos AL ====================
# Memory proxy registration
memProxy = ALProxy("ALMemory",IP,PORT)
if memProxy is None:
    log.error("Could not get a proxy to ALMemory on %s:%d", IP, PORT)
    exit(1)

# AduioDevice proxy registration
audioDeviceProxy = ALProxy("ALAudioDevice",IP,PORT)
if audioDeviceProxy is None:
    log.error("Could not get a proxy to ALAudioDevice on %s:%d", IP, PORT)
    exit(1)


# ==================== Lecuta de Energía promedia en un bufer de 170 ms ====================
#Habilitamos la computación de la energía
audioDeviceProxy.enableEnergyComputation()

#Leemos la energía
print "Energía del microfono izquierdo: "+str(audioDeviceProxy.getLeftMicEnergy ())
print "Energía del microfono derecho: "+str(audioDeviceProxy.getRightMicEnergy ())
print "Energía del microfono frontal: "+str(audioDeviceProxy.getFrontMicEnergy ())
print "Energia del microfono trasero: "+str(audioDeviceProxy.getRearMicEnergy())

#Desabiitmaos la computaicón de la energía
audioDeviceProxy.disableEnergyComputation()

# ==================== Parámetros internos ====================
# Obtencion de parámetros internos (inputBufferSize,outputSampleRate)
print "Tamaño del buffer de entrada: "+str(audioDeviceProxy.getParameter('inputBufferSize')) #Desactualizado desde la vesión 1.22
outSR = audioDeviceProxy.getParameter('outputSampleRate')
if (outSR == -1  ):
    print "Parámetro de entrada no válido, solo se acepta: \n\t- inputBufferSize\n\t-outputSampleRate"
else:
    print "Muestra de la tasa de salida: "+str(outSR)

#Modificación de los parámetros internos (Valores discretos)
# outputSampleRate -> [16000, 22050, 44100, 48000] Hz
# inputBufferSize -> [8192, 16384] >>> Obsoleto desde la versión 1.22
audioDeviceProxy.setParameter('outputSampleRate',48000)
outSR = audioDeviceProxy.getParameter('outputSampleRate')
print "Nueva tasa de saldia: "+str(outSR)
audioDeviceProxy.setParameter('outputSampleRate',44100)
# ==================== Volumen de salida general del sistema ====================
print "Volumen de salida [0,100] (defaul: 90): "+str(audioDeviceProxy.getOutputVolume())
audioDeviceProxy.setOutputVolume(30)
print "Nuevo volumen de salida: "+str(audioDeviceProxy.getOutputVolume())
audioDeviceProxy.setOutputVolume(90)

# ==================== Limpiar muestras que se envía al altavoz ====================
audioDeviceProxy.flushAudioOutputs()

# ==================== Silenciar el dipositivo de salida ====================
print "Disposivo de salda, mutado: "+str(audioDeviceProxy.isAudioOutMuted())
audioDeviceProxy.muteAudioOut(True) #[True, False]
print "Disposivo de salda, mutado: "+str(audioDeviceProxy.isAudioOutMuted())
audioDeviceProxy.muteAudioOut(False) #[True, False]


# ==================== Grabar audio ====================

tts = audio = record = aup = None 
# ----------> Connect to robot <----------
try: 
    tts = ALProxy("ALTextToSpeech", IP, PORT)
    audio = ALProxy("ALAudioDevice", IP, PORT)
    record = ALProxy("ALAudioRecorder", IP, PORT)
    aup = ALProxy("ALAudioPlayer", IP, PORT)
except Exception, e:
    print "Error al conectar con el robot."
    log.error(""+e)
# ----------> recording <----------
print 'start recording...'
record_path = '.\recordings\microphones\recording.wav'
record.startMicrophonesRecording(record_path, 'wav', 48000, (1,1,1,1))
time.sleep(5)
record.stopMicrophonesRecording()
print 'record over'

#Reproducimos el audio grabado
fileID = aup.playFile(record_path, 0.7, 0)


# ==================== Leer los datos de un archivo ====================
audioDeviceProxy.setFileAsInput(record_path)
