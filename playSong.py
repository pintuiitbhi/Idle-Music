#! /usr/bin/env python3
import os, dbus,time
from random import randint

def play_song():
    file = open("/home/pintu/.song_list.txt","r")
    songsList = file.read().splitlines()
    file.close()
    sum=0
    num_songs=0
    for i in songsList:
        if i.isdigit():
            sum=sum+ int(i)
        num_songs+=1

    avg = sum/num_songs

    while (True):
        randomSong = randint(0,len(songsList)-1)
        if randomSong % 2 == 0:
            if int(songsList[randomSong]) > avg:
                os.popen("vlc "+'"'+songsList[randomSong+1]+'"')
                break

def screensaver_active():
    session_bus = dbus.SessionBus()
    gnome_screensaver = 'org.gnome.ScreenSaver'
    object_path = '/{0}'.format(gnome_screensaver.replace('.', '/'))
    get_object = session_bus.get_object(gnome_screensaver, object_path)
    get_interface = dbus.Interface(get_object, gnome_screensaver)
    status = bool(get_interface.GetActive())
    return status



if __name__ == "__main__":
    while 1:
        variable = screensaver_active()
        if variable == True:
            play_song()
            time.sleep(60)
            os.popen("pkill vlc")
