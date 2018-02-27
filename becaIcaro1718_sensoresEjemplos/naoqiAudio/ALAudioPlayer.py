# -*- encoding: UTF-8 -*-
'''
Created on 27 feb. 2018
API de AudioPlayer
Clase generada apartir de http://doc.aldebaran.com/2-4/naoqi/audio/alaudioplayer.html
@author: Andres Ruiz  Pe�uela
@fecha: 180227
@version: 0.0.1
'''
import qi
from naoqi import ALProxy
import logging as log

class ALAudioPlayer (object):
    
    def __init__(self,IP="127.0.0.1",PORT=9559):
        #Construcctor inicial
        self.IP = IP
        self.PORT = PORT
        self.proyAPlayer = None
        #self.session = qi.Session()
        #self.session.connect("tcp://" + self.IP + ":" + str(self.PORT))
    
    def conexion(self):
        #Método para establecer la coneixón con la API de AudioPlayer
        try:
            #self.proxyAPlayer = ALProxy("ALAudioPlayer") #Cuando se ha establecido na sesión previamente
            self.proxyAPlayer = ALProxy("ALAudioPlayer", self.IP, self.PORT)
        except Exception, e:
            log.error("No se ha podido conectar, "+e)
    
     def loadFile(self, fileName):
        """
        Carga el 
        Loads a file for ulterior playback
        :param str fileName: Path of the sound file (either mp3 or wav)
        :returns int: Id of the file which has been loaded. This file can then be played with the play function
        """
        if not self.proxy:
            self.proxy = ALProxy("ALAudioPlayer")
        return self.proxy.loadFile(fileName)
    
    def getCurrentPosition(self,playId):
        """
        Devuelve la posición en segundos del archivo repoducido acutal
        @param int playId: Identificador del proceso que se está reproducciendo
        @return float: Posición del archivo en segundos
        """
        if not self.proxyAPlayer:
            self.conexion()
            
        return self.proxyAPlayer.getCurrentPosition(playId)
    
    def getVolume(self, playId):
        """
        Devuelve el volumen de la reproducción.
        @param int playId: Identificador del proceso que esta reproduciendo el archivo.
        @returns float: Volumen de la reproducción [0.0 ~ 1.0 ]
        """
        if not self.proxy:
            self.proxy = ALProxy("ALAudioPlayer")
        return self.proxy.getVolume(playId)