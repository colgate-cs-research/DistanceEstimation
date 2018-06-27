from scapy.all import RadioTap, Dot11Elt, Dot11ProbeReq, Dot11, sr

iface = 'wlp2s0'   #Interface name here

packet = RadioTap()/Dot11(addr1="ff:ff:ff:ff:ff:ff",addr2="c8:f7:33:da:b1:e1",addr3="ff:ff:ff:ff:ff:ff")/Dot11ProbeReq()/Dot11Elt(ID="SSID")
resp = sr(packet, iface=iface)
