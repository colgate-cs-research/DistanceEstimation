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

**Packet Types:**

- Beacon Frame: type 0, subtype 8


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

