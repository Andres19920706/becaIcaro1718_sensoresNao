# -*- encoding: UTF-8 -*-
# http://doc.aldebaran.com/2-1/dev/python/examples/vision/get_image.html#visualize-live-nao-images-using-pyqt
# This is just an example script that shows how images can be accessed
# through ALVideoDevice in python.
# Nothing interesting is done with the images in this example.

from naoqi import ALProxy
import vision_definitions
import time

IP = "192.168.1.39"  # Replace here with your NAOqi's IP address.
PORT = 9559

####
# Create proxy on ALVideoDevice

print "Creating ALVideoDevice proxy to ", IP

camProxy = ALProxy("ALVideoDevice", IP, PORT)

####
# Register a Generic Video Module

resolution = vision_definitions.kQQVGA
colorSpace = vision_definitions.kYUVColorSpace
fps = 20

nameId = camProxy.subscribe("python_GVM", resolution, colorSpace, fps)

print 'getting images in remote'
for i in range(0, 20):
  print "getting image " + str(i)
  camProxy.getImageRemote(nameId)
  time.sleep(0.05)

camProxy.unsubscribe(nameId)