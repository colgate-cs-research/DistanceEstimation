Passively Finding Distance Between an Access Point & a Mobile Device
=======================

This is a WIP research work by Muhammad Yasoob Ullah Khalid and Aaron Gember-Jacobson from Colgate University. We are trying to find a novel way to passively measure the distance between a mobile device and an access point.

The research paper can be found in the `paper` folder. If you have any ideas/comments/suggestions please let us know. We can be reached at:

- Yasoob (ykhalid at colgate.edu)
- Aaron  (agemberjacobson at colgate.edu)

**Important Commands:**

- `nmcli dev wifi` for searching Wi-Fi on ubuntu
- `sudo ifconfig wlp2s0 down` take down the interface
- `sudo iwconfig wlp2s0 mode monitor` put the interface into monitor mode
- `sudo ifconfig wlp2s0 up` put the interface back up
- `sudo iwconfig wlp2s0 mode managed` put the interface into managed mode
- `sudo iwlist wlp2s0 scanning` actively scan nearby Wi-Fi networks
- `sudo nmcli device wifi hotspot con-name my-hotspot ssid my-hotspot band bg password thisissocool` for setting hotspot through command-line
- `sudo nmcli device disconnect wlp2s0` convert Wi-Fi card back to managed mode

**Packet Types:**

- Beacon Frame: type 0, subtype 8

**Wireshark Filters**

http://wifinigel.blogspot.com/2018/04/wireshark-capture-filters-for-80211.html

**Sending & Sniffing Auth Requests**

You put the Wi-Fi card in monitor mode:

```
sudo ifconfig wlp2s0 down
sudo iwconfig wlp2s0 mode monitor
sudo ifconfig wlp2s0 up
```

You create an Auth packet using the following command:

```
Dot11(addr1=receiver, addr2=sender, addr3=receiver) / Dot11Auth(algo=0, seqnum=0x0001, status=0x0000)
```

You add a RadioTap header at the beginning and use the following command to send the packet:

```
send(frame)
```
 
On the sniffing PC, you put the Wi-Fi card into monitor mode:

```
sudo ifconfig wlp2s0 down
sudo iwconfig wlp2s0 mode monitor
sudo ifconfig wlp2s0 up
```

You filter those incoming packets which have `Dot11Auth` layer. This will filter the sender AND the receiver device because the receiver sends an Auth response and that too contains `Dot11Auth` layer.

Sender: `auth_frame.py`
Sniffer: `auth_sniffer.py`

-----------------------

Problems
-------

I have managed to send RTS frames. The RTS code is in `rts_frame.py` file. Initially I thought that my sender isn't working properly because my sniffer `rts_sniffer.py` wasn't giving any output. Then I used tcpdump to record and filter rts/cts frames and the frames sent from my MAC address were visible.

- Command for sniffing:

```
sudo tcpdump -i wlp2s0 -s 0 -w test.pcap -Z ykhalid
```

- Command for filtering:

```
tcpdump -r test.pcap "subtype cts or subtype rts"
```

- Recorded response sample:

```
reading from file test.pcap, link-type IEEE802_11_RADIO (802.11 plus radiotap header)
00:49:50.326884 1.0 Mb/s 2412 MHz 11b -18dBm signal antenna 3 Request-To-Send TA:c8:f7:33:da:b1:e1 (oui Unknown) 
00:49:50.327213 1.0 Mb/s 2412 MHz 11b -16dBm signal antenna 3 Clear-To-Send RA:c8:f7:33:da:b1:e1 (oui Unknown) 
00:49:50.327768 1.0 Mb/s 2412 MHz 11b -18dBm signal antenna 3 Request-To-Send TA:c8:f7:33:da:b1:e1 (oui Unknown) 
00:49:50.328095 1.0 Mb/s 2412 MHz 11b -16dBm signal antenna 3 Clear-To-Send RA:c8:f7:33:da:b1:e1 (oui Unknown) 
00:49:50.329634 1.0 Mb/s 2412 MHz 11b -18dBm signal antenna 3 Request-To-Send TA:c8:f7:33:da:b1:e1 (oui Unknown) 
00:49:50.329960 1.0 Mb/s 2412 MHz 11b -16dBm signal antenna 3 Clear-To-Send RA:c8:f7:33:da:b1:e1 (oui Unknown) 
00:49:50.331063 1.0 Mb/s 2412 MHz 11b -18dBm signal antenna 3 Request-To-Send TA:c8:f7:33:da:b1:e1 (oui Unknown) 
```

My question is: Are the aforementioned CTS frames sent by my hotspot? If not then why isn't my hotspot returning any CTS frame?
