# -*- encoding: UTF-8 -*-
from SoundLocalization import ALSoundLocatlization
from Memory import ALMemory
import time
import logging as Log

SoundLoc = ALSoundLocatlization("192.168.1.39")
MemoryProxy = ALMemory("192.168.1.39")

#Conectamos con NAO
try:
    SoundLoc.conection()
    MemoryProxy.connection
except Exception, e:
    Log.error("Server>>\n"+str(e))

#Comprobmaos la verisón de NAOqi
Log.warning("Version NAOqi: "+str(SoundLoc.version()))

#Comprobamos el estado del a conexión
if SoundLoc.ping():
    print "Conexión ALSoundLocatlizationProxy establecida"

#Vemos la lista de eventos actuales en ALMemory
print SoundLoc.getEventList()

#Nos subscrimos para generar el evento ALMoundLocalization/SoundLocated "ALMemory" 
SoundLoc.subscribe2("Andres")

MemoryProxy.subscribeToMicroEvent()

time.sleep(10)

print "Fin"
#Anulamos la subscripción para dejar de generar el evento ALMoundLocalization/SoundLocated "ALMemory" 
#SoundLoc.unsubscribe("Andres")


#exit(1)
#C
