import os
mac ="00:58:56:4C:2F:2F"
from bluetool import Bluetooth
from time import sleep

bluetooth = Bluetooth()
print("Scanning started...")
bluetooth.scan()
print("Scanning completed...")
devices = bluetooth.get_available_devices()
print("Available devices")
print(devices)

print("pairing with",mac)
if bluetooth.pair(mac):
    print("Pairing completed")
    sleep(7)
else:
    print("Unable to Pair")
    exit(1)
print("Connecting with",mac)
if bluetooth.connect(mac):
    print("Connected successfully!")
else:
    print("Unable to connect")

# Playing audio

# for i in range(3):
 #    os.system("mpg123 Kaathalae_Kaathalae-SunMusiQ.Com.mp3 ")
  #   sleep(10)

play_duration = 60
interval = 10

import vlc
for i in range(1,4):
    player=vlc.MediaPlayer("/home/user/bt_automation/Yaanji Yaanji.mp3")
    print i ,"Playing"
    player.play()
    sleep(play_duration)
    # print "Pausing"
    # player.pause()
    # print "Paused"
    # sleep(5)
    # print "Playing again"
    # player.play()
    # sleep(30)
    # print "Stopping"
    player.stop()
    print i,"Stopped"
    sleep(interval)