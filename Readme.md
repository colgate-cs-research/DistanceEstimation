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

