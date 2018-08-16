import time
from bluetool import Bluetooth
bluetooth = Bluetooth()
print("Scanning started...")
bluetooth.scan()
mac = "01:01:01:01:0D:DE"
print("Scanning completed...")
devices = bluetooth.get_available_devices()
print("Available devices")
print(devices)

print("pairing with mac address")
if bluetooth.pair(mac):
    print("Pairing completed")
    time.sleep(15)
    print("Connecting with ",mac)
    if bluetooth.connect(mac):
       print("Connected successfully!")
    else:
       print("Unable to connect")
else:
    print("Unable to Pair")
    exit()

