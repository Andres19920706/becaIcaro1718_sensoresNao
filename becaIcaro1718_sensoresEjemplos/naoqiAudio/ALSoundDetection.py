# -*- encoding: UTF-8 -*-
'''
Created on 27 feb. 2018
API de AudioPlayer
El módulo ALSoundDetection detecta sonidos significativos en los buffers de audio entrantes
Esta detección se basa en el nivel de señal de audio y, como tal, se comporta de manera similar en cualquier tipo de sonido (siempre que sea lo suficientemente alto).

Clase generada apartir de http://doc.aldebaran.com/2-4/naoqi/audio/alsounddetection.html
@info: http://ii.tudelft.nl/naodoc/site_en/reddoc/audio_system/Overview_ALSoundDetection.html
En la versión 2.4., esta API solo es accedida como servicio.
@author: Andres Ruiz  Pe�uela
@fecha: 180227
@version: 0.0.1
'''

from naoqi import ALProxy
import logging as log
import sys
import time
proxy = ALProxy("ALSoundDetection", "192.168.1.39", 9559)
'''
Cambia la sensibilidad de la detección
@return None: Si el cabmio ha sido satisfactorio
'''
proxy.setParameter("Sensibility", 0.9)
proxy.setParameter("Sensitivity", 0.9)

'''
Obtiene el período actual.
:return int: periodo de actualización (en milisegundos).
'''
print proxy.getCurrentPeriod()

'''
Obtiene la precisión actual.
:return float: Precisión del extractor.
'''
print proxy.getCurrentPrecision()

'''
Obtener la lista de eventos actualizados en ALMemory.
:return std :: vector <std :: string>: matriz de eventos actualizada por este extractor en ALMemory
'''
print proxy.getEventList()

'''
Obtener la lista de eventos actualizados en ALMemory.
:return std :: vector <std :: string>: matriz de eventos actualizada por este extractor en ALMemory
'''
print proxy.getMemoryKeyList()

'''
Susbribe un módulo
proxy.subscribe (nombre, período, precisión)
o
proxy.subscribe (nombre)

ifnormaci obetnido en getData
[[index_1, type_1, confidence_1, time_1],
 ...,
[index_n, type_n, confidence_n, time_n]]

índice: es el índice de los puntos de inicio y final de un sonido detectado.
tipo: contiene 1 para el punto de inicio y 0 para el punto final.
confianza: proporciona una estimación de la probabilidad [0; 1] de que el sonido detectado por el módulo corresponda a un sonido real.
tiempo: es el tiempo de detección en micro segundos.
'''
#Detecto
proxy.subscribe("SoundDetected",1,0.3)
#proxy.subscribe("SoundDetected")
print "EE: "+str(proxy.getOutputNames())
time.sleep(5)
memory = ALProxy("ALMemory", "192.168.1.39", 9559)
print memory.getData("SoundDetected") #
proxy.unsubscribe("SoundDetected")
'''
Version del módulo 
:return str: Una cadena que contiene la versión del módulo.
'''
print proxy.version()