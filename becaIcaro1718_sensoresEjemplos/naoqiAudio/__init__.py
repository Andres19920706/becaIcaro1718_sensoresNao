# -*- encoding: UTF-8 -*-
from ALAudioPlayer import ALAudioPlayer


audioPlay = ALAudioPlayer("192.168.1.39",9559)
print audioPlay.IP
print audioPlay.PORT
print audioPlay.ping()