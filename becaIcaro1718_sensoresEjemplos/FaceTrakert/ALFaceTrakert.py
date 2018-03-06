# -*- encoding: UTF-8 -*-
'''
Created on 5 mar. 2018

@author: Andres
'''
from naoqi import ALProxy

class ALFaceTracker(object):
    def __init__(self):
        self.proxy = None
        self.IP = "192.168.1.39"
        self.PORT = 9559

    def force_connect(self):
        self.proxy = ALProxy("ALFaceTracker",self.IP,self.PORT)
        #self.proxy = ALProxy("ALFaceTracker")

    def getPosition(self):
        """Return the [x, y, z] position of the face in FRAME_TORSO. This is done assuming an average face size, so it might not be very accurate.  This invalidates the isNewData field of the tracker. See isNewData()) for more details.
        :returns std::vector<float>: An Array containing the face position [x, y, z].
        """
        if not self.proxy:
            self.proxy = ALProxy("ALFaceTracker",self.IP,self.PORT)
            #self.proxy = ALProxy("ALFaceTracker")
        
        print self.proxy.getPosition()
        #return 