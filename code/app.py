from scapy.all import Dot11,Dot11Beacon,Dot11Elt,RadioTap,sendp,hexdump
netSSID = 'testSSID' #Network name here
iface = 'en0'   #Interface name here

dot11 = Dot11(type=0, subtype=8, addr1='ff:ff:ff:ff:ff:ff',
addr2='22:22:22:22:22:22', addr3='33:33:33:33:33:33')
beacon = Dot11Beacon()
essid = Dot11Elt(ID='SSID',info=netSSID, len=len(netSSID))


frame = RadioTap()/dot11/beacon/essid

frame.show()
print("\nHexdump of frame:")
hexdump(frame)
input("\nPress enter to start\n")

sendp(frame, iface=iface, inter=0.100, loop=1)