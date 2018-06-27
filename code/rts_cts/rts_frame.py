from scapy.all import Dot11,Dot11Beacon,Dot11Elt,RadioTap,sendp,hexdump, Dot11Auth, send

iface = "wlp2s0"
sender = "c8:f7:33:da:b1:e1"  #Cappuccino
receiver = "c8:f7:33:da:6a:e7"   #Frappuccino

#packet = Dot11(addr1=receiver, addr2=sender, addr3=receiver) / Dot11Auth(algo=0, seqnum=0x0001, status=0x0000)
# https://gist.github.com/f00-/e0ad50c5c189a98aaafdc88c5d53c4b4

packet = Dot11(type=1,subtype=11,addr1=receiver,addr2=sender,addr3=receiver,ID=0x99)
frame = RadioTap()/packet

# send(frame)
sendp(frame, iface=iface, inter=0.100, loop=1)
