# -*- encoding: UTF-8 -*-
'''
Created on 5 mar. 2018

ALSoundLocalization identifica la dirección de cualquier sonido 
suficientemente fuerte que escuche el robot.
@author: Andres Ruiz Peñuela
@version: 0.0.1
'''
from naoqi import ALProxy
import logging as Log
import sys

class ALSoundLocatlization(object):
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
        Generamos la clase ALSoundLocalizationProxy, para establecer conexión con NAO
        '''
        Log.warning("Conectando a NAO ... "+str(self.IP)+":"+str(self.PORT))
        self.PROXY = ALProxy("ALSoundLocalization",self.IP,self.PORT)#
         
        

    # ================== métodos heredados de ALModule API ==================
    def getCurrentPeriod(self):
        """
        Devuelve el perido con el que mira el buffer
        @return int: periodo de actualización en ms
        """
        out = None
        try:
            if not self.PROXY:
                self.conection()
            out = self.PROXY.getCurrentPeriod()
        except Exception, e:
            Log.error("Server>>\n"+str(e))
        
        return out

    def getCurrentPrecision(self):
        """
        Devuelve la precisión actual del extractor
        :return float: Precisión del extractor
        """
        try:
            if not self.PROXY:
                self.conection()
            out = self.PROXY.getCurrentPrecision()  
        except Exception, e:
            Log.error("Server>>\n"+str(e))
            
        return out  
    
    def  getEventList ( self ):
        """ 
        Obtener la lista de eventos actualizados en ALMemory.
        :return vector <string>: Matriz de eventos actualizada para el extractor acutal en ALMemory ['ALSoundLocalization/SoundLocated', 'ALSoundLocalization/SoundsLocated']
        """
        out = None
        try:
            if not self.PROXY:
                self.conection()
            out = self.PROXY.getEventList() 
        except Exception, e:
            Log.error("Server>>\n"+str(e))
                     
        return out  
    
    def getMemoryKeyList(self):
        """
        Devuelve la lista de eventos actualiza en ALMemrory.
        :return vector<string>: Vector de ecentos acutalizaso por el extrator actula den ALMemory
        """
        out = None
        try:
            if not self.PROXY:
                self.conection()
            out = self.PROXY.getMemoryKeyList()   
        except Exception, e:
            Log.error("Server>>\n"+str(e))
            
        return out  
    
    def getMyPeriod(self, name):
        """
        Devuelve el perdio de una subcripción específica.
        :param name: Nombre del módulo subscripto.
        :return int: Perido de actualizaicón en ms.
        """
        out = None
        try:
            if not self.PROXY:
                self.conection()
            out = self.PROXY.getMyPeriod(name)   
        except Exception, e:
            Log.error("Server>>\n"+str(e))
            
        return out  
    
    def getMyPrecision(self, name):
        """
        Devuelve la precisón de una subcripción específica.
        :param name: Nombre del módulo subscripto.
        :return float: Precisión del extractor.
        """
        out = None
        try:
            if not self.PROXY:
                self.conection()
            out = self.PROXY.getMyPrecision(name)
        except Exception, e:
            Log.error("Server>>\n"+str(e))
            
        return out  
    
    def getOutputNames(self):
        """
        Devuelve la lista de envetos actualizaos en ALMemory.
        :return vector<string>: Vectro de valores actualizaso por el extractor actual en ALMemory.
        """
        out = None
        try:
            if not self.PROXY:
                self.conection()
            out = self.PROXY.getOutputNames()   
        except Exception, e:
            Log.error("Server>>\n"+str(e))
            
        return out  

    def getSubscribersInfo(self):
        """
        Devuele los parámetros contenido en el módulo.
        :return ALValue: Vector de nombres y parámetros de todas las subcripciones.
        """
        out = None
        try:
            if not self.PROXY:
                self.conection()
            out = self.PROXY.getSubscribersInfo()    
        except Exception, e:
            Log.error("Server>>\n"+str(e))
            
        return out
    
    def ping(self):
        """
        Comprueba la conectivadad con NAO. Siempbre devuelve True.
        :returns bool: True si esta conectado
        """
        out = None
        try:
            if not self.PROXY:
                self.conection()
            out = self.PROXY.ping()  
        except Exception, e:
            Log.error("Server>>\n"+str(e))
            
        return out
    
    def version(self):
        """
        Devuelve la versión del módulo.
        :returns str: Un string con la versión del módulo
        """
        out = None
        try:
            if not self.PROXY:
                self.conection()
            out = self.PROXY.version() 
        except Exception, e:
            Log.error("Server>>\n"+str(e))
            
        return out
    
    def subscribe(self, name, period, precision):
        """
        Subscripción con valores de periodo y precisión dados a ALSoundLocalizationProxy.
        Esto hace que el módulo comience a generar el evento ALMoundLocalization/SoundLocated "ALMemory" 
        al que puede suscribirse utilizando ALMemoryProxy::subscribeToMicroEvent.
        :param str name: Nombre para identificar al subscriptro.
        :param int period: Periodo de actualizacion en ms.
        :param float precision: Precisión del extractor.
        """
        try:
            if not self.PROXY:
                self.conection()
            self.PROXY.subscribe(name, period, precision)
            Log.warning("Subscripición de "+str(name)+" establecidad.")
        except Exception, e:
            Log.error("Server>>\n"+str(e))

    def updatePeriod(self, name, period):
        """
        Actualiza el perido de un subscriptor.
        :param str name: Nombre del módulo con el que se ha subscripto.
        :param int period: Periodo de actualización en ms.
        """
        try:
            if not self.PROXY:
                self.conection()
            self.PROXY.updatePeriod(name, period)
        except Exception, e:
            Log.error("Server>>\n"+str(e))

    def updatePrecision(self, name, precision):
        """
        Actualiza de la precisión de un subscriptor.
        :param str name:Nombre del módulo con el que se ha subscripto.
        :param float precision: Precision del modulo subscirpto.
        """
        try:
            if not self.PROXY:
                self.conection()
            self.PROXY.updatePrecision(name, precision)
        except Exception, e:
            Log.error("Server>>\n"+str(e))

    # ================== métodos heredados de API ALVisionExtractor =================
    def isPaused(self):
        """
        Devuelve el estado actual de pausa del extractor .
        :return bool: True si el extractor esta pausado, False en caso contrarIo.
        """
        out = None
        try:
            if not self.PROXY:
                self.conection()
            out = self.PROXY.isPaused()   
        except Exception, e:
            Log.error("Server>>\n"+str(e))
            
        return out

    def isProcessing(self):
        """
        Devuelve el estado de ejcución del extractor.
        :return bool: True si el extractor esta procesando imagnes actualmente, False en caso contrario.
        """
        out = None
        try:
            if not self.PROXY:
                self.conection()
            out = self.PROXY.isProcessing()  
        except Exception, e:
            Log.error("Server>>\n"+str(e))
            
        return out
    
    def pause(self, status):
        """
        Cambia el estado pausa del extractor.
        :param bool status: TRUE pausar el extractor, False para activar el extractor.
        """
        try:
            if not self.PROXY:
                self.conection()
            self.PROXY.pause(status) 
        except Exception, e:
            Log.error("Server>>\n"+str(e))
            
    
    # ================== métodos heredados de ALSoundLocalizationProxy =================
    def setParameter(self, parameter, value):
        """
        Cambia el valor de un paráemtro específicoSet the specified parameter.
        :param str parameter: Nombre del parámetro. ["Sensibility" <=> "Sensitivity","EnergyComputation"]
        :param ALValue value: "Sensibility" o "Sensitivity" ->  float [0,1]. "EnergyComputation" -> (1 o 0).
        """
        try:
            if not self.PROXY:
                self.conection()
            self.PROXY.setParameter(parameter, value)
        except Exception, e:
            Log.error("Server>>\n"+str(e))
    
    def subscribe2(self, name):
        """
        Heredado de ALModule
        Subscripción a ALSoundLocalizationProxy.
        Esto hace que el módulo comience a generar el evento ALMoundLocalization/SoundLocated "ALMemory". 
        al que puede suscribirse utilizando ALMemoryProxy::subscribeToMicroEvent.
        :param str name: Nombre para identificar al subscriptro.
        :param int period: Periodo de actualizacion en ms.
        :param float precision: Precisión del extractor.
        """
        try:
            if not self.PROXY:
                self.conection()
            self.PROXY.subscribe(name)
            Log.warning("Subscripición de "+str(name)+" establecida.")
        except Exception, e:
            Log.error("Server>>\n"+str(e))
    
    def unsubscribe(self, name):
        """
        Heredado de ALModule
        Anula la subscripción de ALSoundLocalizationProxy.
        Esto hace que el módulo deje de generar el evento ALMoundLocalization/SoundLocated "ALMemory".
        :param str name: Nombre del modulo con el que se subscribió.
        """
        try:
            if not self.PROXY:
                self.conection()
            self.PROXY.unsubscribe(name)
            Log.warning("Subscripición de "+str(name)+" anulada.")
        except Exception, e:
            Log.error("Server>>\n"+str(e))
    
    # ================== Lista de eventos =================