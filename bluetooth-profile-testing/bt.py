from bluetool import Bluetooth
from time import sleep
bluetooth = Bluetooth()
print("Scanning started...")
bluetooth.scan()
print("Scanning completed...")
devices = bluetooth.get_available_devices()
print("Available devices")
print(devices)

print("pairing with D8:32:E3:38:02:9D")
if bluetooth.pair('D8:32:E3:38:02:9D'):
    print("Pairing completed")
    sleep(7)
else:
    print("Unable to Pair")
    exit(1)
print("Connecting with D8:32:E3:38:02:9D")
if bluetooth.connect('D8:32:E3:38:02:9D'):
    print("Connected successfully!")
else:
    print("Unable to connect")
