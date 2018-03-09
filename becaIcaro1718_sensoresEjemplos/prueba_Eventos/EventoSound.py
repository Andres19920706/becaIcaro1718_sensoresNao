# -*- encoding: UTF-8 -*-
'''
Created on 9 mar. 2018

@author: Andres
'''
import sys
import time

from naoqi import ALProxy
from naoqi import ALModule

from PIL import Image

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
        
        print "Sonido detectado"
        x = memory.getData("ALSoundLocalization/SoundLocated")
        print "Datos obtenidos: "+str(x[1])
        print "Azimut: "+str(x[1][0])+"rad, "+str(x[1][0]*3.141516/180)+"�"
        print "Altitud: "+str(x[1][1])+"rad, "+str(x[1][1]*3.141516/180)+"�"
        print "Confizanza de voz humana: "+str(x[1][2])
        print "Energía: "+str(x[1][3])
        
        # Posiciones de las articulaciones
        headPitch = memory.getData("Device/SubDeviceList/HeadPitch/Position/Actuator/Value")
        headYaw = memory.getData("Device/SubDeviceList/HeadYaw/Position/Actuator/Value")
        print "HEAD_PITCH: "+str(headPitch)
        print "HEAD_YAW: "+str(headYaw)
        
        """"
        # -------------- extracción de imagen -----------------
        camProxy = ALProxy("ALVideoDevice")
        resolution = 2    # VGA
        colorSpace = 11   # RGB
        
        videoClient = camProxy.subscribe("python_client", resolution, colorSpace, 5)

        t0 = time.time()
        naoImage = camProxy.getImageRemote(videoClient)

        t1 = time.time()
        print "acquisition delay ", t1 - t0

        camProxy.unsubscribe(videoClient)
        imageWidth = naoImage[0]
        imageHeight = naoImage[1]
        array = naoImage[6]

        # Create a PIL Image from our pixel array.
        im = Image.frombytes("RGB", (imageWidth, imageHeight), array)

        # Save the image.
        im.save("camImage.png", "PNG")

        im.show()
        # -----------------------------------------------------
        """
        # Unsubscribe to the event when talking,
        # to avoid repetitions
        memory.unsubscribeToEvent("SoundDetected",
            "HumanSound")

        self.tts.say(" e")

        # Subscribe again to the event
        memory.subscribeToEvent("SoundDetected",
            "HumanSound",
            "onSoundDetected")