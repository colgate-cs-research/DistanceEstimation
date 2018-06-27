#!/usr/bin/env python

from scapy.all import *

ap_list = []

def PacketHandler(pkt) :
    if pkt.haslayer(Dot11) :
        if pkt.type == 11 and pkt.subtype == 12:
            if pkt.addr2 not in ap_list:
                ap_list.append(pkt.addr2)
                print "AP MAC: %s with SSID: %s " %(pkt.addr2, pkt.info)


sniff(iface="wlp2s0", prn = PacketHandler)
