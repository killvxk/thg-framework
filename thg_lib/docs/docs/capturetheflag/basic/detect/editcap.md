## Use to edit a pcap file (split into 1000 packets):
```
editcap -F pcap -c 1000 orignal.pcap
```
## out_split,pcap Use to edit a pcap file (split into 1 hour each packets):
```
editcap -F pcap -t+3600 orignal.pcap out_split.pcap
```