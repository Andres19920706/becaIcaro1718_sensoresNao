# -*- encoding: UTF-8 -*-
'''
Created on 5 mar. 2018

@author: Andres
'''
from naoqi import ALProxy
import logging as Log
import sys

class ALMemory(object):
    '''
    Clase con los métodos del módulo ALSoundLocalizaton
    '''
    IP = None #Dirección IP de NAO
    PORT = None #Puerto de NAO
    PROXY = None #Conexión con NAO
    
    def __init__(self, ip="127.0.0.1", port=9559):
        '''
        Constructor inicial
        '''
        self.IP = ip     
        self.PORT = port
    
    def conection(self):
        '''
        Generamos la clase ALMemeroyProxy, para establecer conexión con NAO
        '''
        Log.warning("Conectando a NAO ... "+str(self.IP)+":"+str(self.PORT))
        self.PROXY = ALProxy("ALMemory",self.IP,self.PORT)#
    
     # ================== métodos heredados de ALMemoryProxy =================
    def getSubscribers(self,name):
        """
        Obtiene una lista que contiene los nombres de los suscriptores de un evento
        @param str name: Nombre del evento o microevento
        @return Lista de nombres de subscriptores
        """
        out = None
        try:
            if not self.PROXY:
                self.conection()
            out = self.PROXY.getSubscribers(name)
        except Exception, e:
            Log.error("Server>>\n"+str(e))
        
        return out
    
    def getData(self):
        out = None
        try:
            if not self.PROXY:
                self.conection()
            out = self.PROXY.getData("ALSoundLocalization/SoundLocated")
        except Exception, e:
            Log.error("Server>>\n"+str(e))
        
        return out
        
    def getMicroEventList(self ):
        """
        Obtiene una lista que contiene los nombres de todos los micro-eventos declarados.
        
        :return Lista de los nombres 
        """
        out = None
        try:
            if not self.PROXY:
                self.conection()
            out = self.PROXY.getMicroEventList()
        except Exception, e:
            Log.error("Server>>\n"+str(e))
        
        return out
    
    def subscribeToMicroEvent(self):
        out = None
        try:
            if not self.PROXY:
                self.conection()
            print "entro"
            out = self.PROXY.subscribeToMicroEvent("prueba", "res", "message", "pythondatachanged")
            print "salgo"
        except Exception, e:
            Log.error("Server>>\n"+str(e))
        
        return out

# create python module
class myModule():
  """python class myModule test auto documentation"""


  def pythondatachanged(self, strVarName, value,message):
    """callback when data change"""
    print "Micro-event is raise callback is called by ALMemory"
    print value
    #print "datachanged", strVarName, " ", value, " ", strMessage
