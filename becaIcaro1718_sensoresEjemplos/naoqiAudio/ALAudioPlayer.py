# -*- encoding: UTF-8 -*-
'''
Created on 27 feb. 2018
API de AudioPlayer
Clase generada apartir de http://doc.aldebaran.com/2-4/naoqi/audio/alaudioplayer.html
@info: http://ii.tudelft.nl/naodoc/site_en/bluedoc/ALAudioPlayer.html
En la versión 2.4., esta API solo es accedida como servicio.
@author: Andres Ruiz  Pe�uela
@fecha: 180227
@version: 0.0.1
'''

from naoqi import ALProxy
import logging as log
import sys

class ALAudioPlayer (object):
    
    def __init__(self,IP="127.0.0.1",PORT=9559):
        #Construcctor inicial
        self.IP = IP
        self.PORT = PORT
        self.audio_player_service = None
        
    
    def conexion(self,session):
        #Método para establecer la conexión con la API de AudioPlayer    
        try:
            self.audio_player_service = session.service('ALAudioPlayer')
        except Exception, e:
            log.error("\nNo se ha podido conectar, "+str(e))
            sys.exit(1)
    
    def loadFile(self, fileName):
        """
        Carga el aricho para reproducirlo
        :param str fileName: Dirección absoluta del archivo de sonido ( mp3 o wav)
        :returns int: Identificador del archivo que se ha cargado.
        """
        #====
        framemanager = ALProxy("ALFrameManager",self.IP,self.PORT)
        
        #print str( framemanager.getBehaviorPath(self.behaviorId)+"prueba2.wav")
        #=====
        fileId = None
        
        if not self.audio_player_service:
            log.error("\nPara usar este método debes establecer un servicio previo. ")
        else:
            fileId = self.audio_player_service.loadFile(fileName)
            self.audio_player_service.play(fileId, _async=True)
        
        return fileId 
    
    def getCurrentPosition(self,playId):
        """
        Devuelve la posición en segundos del archivo repoducido acutal
        @param int playId: Identificador del proceso que se está reproducciendo
        @return float: Posición del archivo en segundos
        """
        if not self.audio_player_service:
            self.conexion()
            
        return self.audio_player_service.getCurrentPosition(playId)
    
    def getVolume(self, playId):
        """
        Devuelve el volumen de la reproducción.
        @param int playId: Identificador del proceso que esta reproduciendo el archivo.
        @returns float: Volumen de la reproducción [0.0 ~ 1.0 ]
        """
        if not self.audio_player_service:
            self.conexion()
            
        return self.audio_player_service.getVolume(playId)
    
    


        
