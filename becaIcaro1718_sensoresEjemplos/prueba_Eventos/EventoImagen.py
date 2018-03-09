# -*- encoding: UTF-8 -*-
'''
Created on 9 mar. 2018

@author: Andres
'''
import sys
import time

from naoqi import ALProxy
from naoqi import ALBroker
from naoqi import ALModule

from optparse import OptionParser

NAO_IP = "192.168.1.39"

#Cuando detecta un sonido entra al eventeo dice que ha sido heso, y si detecta una cara le sigue.
# Global variable to store the HumanGreeter module instance
HumanGreeter = None
memory = None


class HumanGreeterModule(ALModule):
    """ A simple module able to react
    to facedetection events

    """
    def __init__(self, name):
        ALModule.__init__(self, name)
        # No need for IP and port here because
        # we have our Python broker connected to NAOqi broker

        # Create a proxy to ALTextToSpeech for later use
        self.tts = ALProxy("ALTextToSpeech")

        # Subscribe to the FaceDetected event:
        global memory
        memory = ALProxy("ALMemory")
        memory.subscribeToEvent("SoundDetected",
            "HumanGreeter",
            "onFaceDetected")

    def onFaceDetected(self, *_args):
        """ This will be called each time a face is
        detected.

        """
        print "Sonido detectado"
        x = memory.getData("ALSoundLocalization/SoundLocated")
        print "Datos obtenidos: "+str(x[1])
        print "Azimut: "+str(x[1][0])+"rad, "+str(x[1][0]*3.141516/180)+"�"
        print "Altitud: "+str(x[1][1])+"rad, "+str(x[1][1]*3.141516/180)+"�"
        print "Confizanza de voz humana: "+str(x[1][2])
        print "Energ�a: "+str(x[1][3])
        
        # Unsubscribe to the event when talking,
        # to avoid repetitions
        memory.unsubscribeToEvent("SoundDetected",
            "HumanGreeter")

        self.tts.say("Que ha sido eso? ")

        # Subscribe again to the event
        memory.subscribeToEvent("SoundDetected",
            "HumanGreeter",
            "onFaceDetected")