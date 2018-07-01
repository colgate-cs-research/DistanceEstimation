# Auth Sender & Sniffer

This folder contains code for sending and sniffing auth frames. You can send an auth response by changing `seqnum` to `2`. 

The major difference between the frames produced with `seqnum = 1` and `seqnum = 2` is that with `seqnum = 1` the frame contains 
`Authentication (Open System)-1` and ends with `successful` like this:

```
18:02:06.127085 1.0 Mb/s 2412 MHz 11b -24dBm signal antenna 1 Authentication (Open System)-1: Successful
```

However, with `seqnum = 2` the filtered frame contains `Authentication (Open System)-2` and appears like this:

```
18:00:22.961509 1.0 Mb/s 2412 MHz 11b -24dBm signal antenna 1 Authentication (Open System)-2: 
```

You can use the following tcpdump filter to filter requests:

```
tcpdump -r test.pcap "wlan host c8:f7:33:da:6a:e7"
```

#### File descriptions

- `test_with_seq_1.pcap` contains auth request frames with `seqnum=1`
- `test_with_seq_2.pcap` contains auth request frames with `seqnum=2`
