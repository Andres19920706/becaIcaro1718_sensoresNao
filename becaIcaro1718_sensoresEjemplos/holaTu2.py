# -*- encoding: UTF-8 -*-
""" 
Say 'hello, you' each time a sound is detected
"""

import sys
import time

from naoqi import ALProxy
from naoqi import ALBroker
from naoqi import ALModule

from optparse import OptionParser

NAO_IP = "192.168.1.39"


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
        print "Azimut: "+str(x[1][0])+"rad, "+str(x[1][0]*3.141516/180)+"º"
        print "Altitud: "+str(x[1][1])+"rad, "+str(x[1][1]*3.141516/180)+"º"
        print "Confizanza de voz humana: "+str(x[1][2])
        print "Energía: "+str(x[1][3])
        
        # Unsubscribe to the event when talking,
        # to avoid repetitions
        memory.unsubscribeToEvent("SoundDetected",
            "HumanGreeter")

        self.tts.say("Mooooozaa")

        # Subscribe again to the event
        memory.subscribeToEvent("SoundDetected",
            "HumanGreeter",
            "onFaceDetected")


def main():
    """ Main entry point
    """
    parser = OptionParser()
    parser.add_option("--pip",
        help="Parent broker port. The IP address or your robot",
        dest="pip")
    parser.add_option("--pport",
        help="Parent broker port. The port NAOqi is listening to",
        dest="pport",
        type="int")
    parser.set_defaults(
        pip=NAO_IP,
        pport=9559)

    (opts, args_) = parser.parse_args()
    pip   = opts.pip
    pport = opts.pport

    # We need this broker to be able to construct
    # NAOqi modules and subscribe to other modules
    # The broker must stay alive until the program exists
    myBroker = ALBroker("myBroker",
       "0.0.0.0",   # listen to anyone
       0,           # find a free port and use it
       pip,         # parent broker IP
       pport)       # parent broker port


    # Warning: HumanGreeter must be a global variable
    # The name given to the constructor must be the name of the
    # variable
    global HumanGreeter
    HumanGreeter = HumanGreeterModule("HumanGreeter")

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print
        print "Interrupted by user, shutting down"
        myBroker.shutdown()
        sys.exit(0)



if __name__ == "__main__":
    main()