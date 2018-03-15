# -*- encoding: UTF-8 -*-
'''
Created on 9 mar. 2018

@author: Andres
'''
import sys
import time

import numpy
import math
from naoqi import ALProxy
from naoqi import ALModule

from PIL import Image, ImageDraw, ImageFont

NAO_IP = "192.168.1.39"

# Global variable to store the HumanGreeter module instance



class HumanSoundModule(ALModule):
    """ A simple module able to react
    to facedetection events

    """
    def __init__(self, name):
        # Creamos el módulo, que será usado para el evento.
        ALModule.__init__(self, name)

        # Creamos un proxy de ALTextToSpeech, para su usor posterior, no necesitmoas IP y Puerto
        # porque tenemos creado un broker en Python conectado al broker NAOqi.
        self.tts = ALProxy("ALTextToSpeech")

        # Subscribe to the FaceDetected event:
        global memory
        memory = ALProxy("ALMemory")
        # Suscribmios el evento 
        memory.subscribeToEvent("SoundDetected",
            "HumanSound",
            "onSoundDetected")

    def onSoundDetected(self, *_args):
        """ 
        El método onFaceDetected es llamado cuando detecta un sonido.
        """
        t0 = time.time() #Tiempo en que se detecto el sonido
        # Unsubscribe to the event when talking,
        # to avoid repetitions
        memory.unsubscribeToEvent("SoundDetected",
            "HumanSound")
        
        # ------------------
        print "Sonido detectado"
        x = memory.getData("ALSoundLocalization/SoundLocated")
        print "SoundLocated = "+str(x)
        print "Azimut: "+str(x[1][0])+"rad, "+str(math.degrees(x[1][0]))+" grados"
        print "Altitud: "+str(x[1][1])+"rad, "+str(math.degrees(x[1][1]))+" grados"
        print "Confizanza de voz humana: "+str(x[1][2])
        print "Energía: "+str(x[1][3])
        
        # Posiciones de las articulaciones
        headPitch = memory.getData("Device/SubDeviceList/HeadPitch/Position/Actuator/Value")
        headYaw = memory.getData("Device/SubDeviceList/HeadYaw/Position/Actuator/Value")
        print "HEAD_PITCH: "+str(headPitch)
        print "HEAD_YAW: "+str(headYaw)
        
        # -------------- extracción de imagen -----------------
        camProxy = ALProxy("ALVideoDevice")
        resolution = 2    # kVGA 640x480
        colorSpace = 11 #11   # RGB
        
        videoClient = camProxy.subscribe("python_client", resolution, colorSpace, 5)

        #t0 = time.time()
        naoImage = camProxy.getImageRemote(videoClient)

        t1 = time.time() #Tiempo en que se obtuvo la imagen
        print "Tiempo trascurrido del sonido a la imagen (s)", t1 - t0

        camProxy.unsubscribe(videoClient)
        imageWidth = naoImage[0]
        imageHeight = naoImage[1]
        array = naoImage[6]

        # Create a PIL Image from our pixel array.
        im = Image.frombytes("RGB", (imageWidth, imageHeight), array)

        
        #Añadimaos punto
        draw = ImageDraw.Draw(im)
        font = ImageFont.truetype("arial.ttf", 60)
        #draw.text((50, 50), "x", font=font, fill="red")
        #y = 1* numpy.sin(x[1][1]*scipy.pi/180)
        #x = 1* numpy.cos(x[1][0]*scipy.pi/180)
        
        AlfaH = math.radians(60.97/2) #Ángulo de visión "azimut"
        AlfaHp = x[1][0] #Ángulo de azimut obtenido [rad] 
        
        AlfaV = math.radians(39) #Ángulo de visión "elevacion"
        AlfaVp = x[1][1] #Ángulo de azimut obtenido [rad]
        #Debu
        if math.fabs(AlfaHp)>AlfaH : print "Fuera del campo de vision horizontal"
        if math.fabs(AlfaVp)>AlfaV : print "Fuera del campo de vision vertial"
        #fin debug
        if(math.fabs(AlfaHp)>AlfaH or math.fabs(AlfaVp)>AlfaV):
            print "Audio fuera del alcanze de vision"
        else:
            #Azimut
            
            npixX = 340*(math.tan(AlfaHp)/math.tan(AlfaH))
            x = (680/2) - npixX


            
            #Elevacion
            npixY = 240*(math.tan(AlfaVp)/math.tan(AlfaV))
            y = 480 + npixY
             


            #Representar punto
            print "npixX= "+str(npixX)+", npixY= "+str(npixY)
            print "Cordeandas -> ("+str(x)+","+str(y)+")"
            draw.text((x,y), ".", font=font, fill="red")
            
            # Save the image.
            im.save("camImagen.png", "PNG")

        #Mostramos
        im.show()
        
        # -----------------------------------------------------
        
        self.tts.say(" e")
        
        # Subscribe again to the event
        memory.subscribeToEvent("SoundDetected",
            "HumanSound",
            "onSoundDetected")
