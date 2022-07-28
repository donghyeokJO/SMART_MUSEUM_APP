#This is a working prototype. DO NOT USE IT IN LIVE PROJECTS

import ScanUtility
import bluetooth._bluetooth as bluez

#Set bluetooth device. Default 0.
# dev_id = 0
# try:
# 	sock = bluez.hci_open_dev(dev_id)
# 	print ("\n *** Looking for BLE Beacons ***\n")
# 	print ("\n *** CTRL-C to Cancel ***\n")
# except:
# 	print ("Error accessing bluetooth")
#
# ScanUtility.hci_enable_le_scan(sock)
# #Scans for iBeacons
# try:
# 	while True:
# 		returnedList = ScanUtility.parse_events(sock, 10)
# 		for item in returnedList:
# 			print(item)
# 			print("")
# except KeyboardInterrupt:
#     pass

async def discover():
    dev_id = 0
    sock = bluez.hci_open_dev(dev_id)
    ScanUtility.hci_enable_le_scan(sock)
    returnedList = ScanUtility.parse_events(sock, 10)

    return returnedList[0]

# import asyncio
# from bleak import BleakScanner
#
# async def discover():
#     devices = await BleakScanner.discover()
#     return devices
