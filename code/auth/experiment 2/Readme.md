- `test_monitor_corrupted.pcap`

I decided to check whether we receive any acknowledgement if I send packets to a random MAC address which
is not near my sender (device). My hypothesis was correct. I didn't receive any acknowledgement for these
packets.
  
- `test_monitor_managed_seq_1.pcap`

I just decided to redo my last experiment to make sure that what I was receiving was actually correct. 
In this experiment I sent auth packets from a sender in monitor mode to a receiver in managed mode. The
experiment was successful and I received acks for the sent packets.
  
- `test_monitor_mobile_seq_1.pcap` 

The is a similar to the above experiment. The only difference is that in this case I sent the packets to mobile
receiver instead of ubuntu. I wanted to check whether the ack behaviour is similar for mobile devices as well 
(which are our main target). The experiment was unsuccessful and I did not receive acks for the sent packets.

- `test_monitor_mobile_wifi_off.pcap`

This is again an edge-case experiment like the first one. In this case the receiver MAC address is near my 
sender but I turned the WIFI in the receiver off. The experiment was successful and I did not receive any
acks for the sent packets.
