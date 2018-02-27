# -*- encoding: UTF-8 -*-
from naoqi import ALProxy
import time
import os

IP = "192.168.1.39"
PORT = 9559

print os.getcwd()
print os.listdir(os.getcwd()) #['ALAUDIODEVICE.py', 'ALAudioPlayer.py', 'ALAudioPlayer.pyc', 'prueba.mp3', 'prueba2.wav', '__init__.py', '__init__.pyc']
#fileId = aup.loadFile(os.getcwd()+"/prueba2.wav")

#time.sleep(5)
#aup.play(fileId)

#Probrar con ruta de linux, si no pedir ayuda en foro
tts = audio = record = aup = None 
# ----------> Connect to robot <----------
try: 
    tts = ALProxy("ALTextToSpeech", IP, PORT)
    audio = ALProxy("ALAudioDevice", IP, PORT)
    record = ALProxy("ALAudioRecorder", IP, PORT)
    aup = ALProxy("ALAudioPlayer", IP, PORT)
except Exception, e:
    print "Error al conectar con el robot."

# ----------> recording <----------

record_path = os.getcwd()+"\prueba2.wav"
#record_path ='./prueba2.wav'
fileId = aup.loadFile(record_path)
#Reproducimos el audio grabado
#fileID = aup.playFile(record_path, 0.7, 0)
aup.play (fileId)

"""

import qi
from ALAudioPlayer import ALAudioPlayer
import sys
import os

audioPlay = ALAudioPlayer("192.168.1.39",9559)
print audioPlay.IP
print audioPlay.PORT
# ========
session = qi.Session()
try:
    session.connect("tcp://" + audioPlay.IP + ":" + str(audioPlay.PORT))
except RuntimeError:
    print ("Can't connect to Naoqi at ip \"" + audioPlay.IP + "\" on port " + str(audioPlay.PORT) +".\n"
           "Comprueba que el cliente este conectado.")
    sys.exit(1)


audioPlay.conexion(session)
dir = str(os.getcwd())
patch = "\naoqiAudio\prueba2.wav"
#print dir+patch
#print os.path.isabs(dir+patch)
#print os.path.abspath(dir+patch)

playId = audioPlay.loadFile(os.path.abspath(dir+patch))
"""
