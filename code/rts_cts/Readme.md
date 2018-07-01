# RTS/CTS Frames

This folder contains code for sending and filtering RTS/CTS frames. Currently as of 1st July, 2018 the sniffer isn't working. However, the sender is working perfectly
fine. You can send the frames using the `rts_frame.py` file. You can filter the frames using tcpdump like this:

```
tcpdump -r test_with_target_managed.pcap "subtype cts or subtype rts"
```

The current problem is that if I try to filter the pcap file using the `host` filter it doesn't give any output. 
