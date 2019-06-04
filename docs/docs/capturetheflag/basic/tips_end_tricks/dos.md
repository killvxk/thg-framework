# FINGERPRINT DOS/DDOS
## Fingerprinting the type of DoS/DDoS:
```
Ref. https://www.trustwave.com/Resources/SpiderLabsBlog/PCAP-Files-Are-Great-Arn-t-They--/
```
## Volumetric: Bandwidth consumption Example, sustaining sending 1Gb of traffic to 10Mb connection
```
Ref. http://freecode.com/projects/iftop
# iftop -n
```
## and Protocol: Use of specific protocol Example, SYN Flood, ICMP Flood, UDP flood
```
# tshark -r <FILE NAME>,pcap -q -z io,phs
# tshark -c 1000 -q -z io,phs
# tcpdump -tn r $FILE I awk -F '. ' '{print $1","$2"."$3","$4}' I sort I uniq -c I sort -n I tail
# tcpdump -qnn "tcp[tcpflags] & (tcp-syn) != 0"
# netstat -s
```
## Example, isolate one protocol and or remove other protocols
```
# tcpdump -nn not arp and not icmp and not udp
# tcpdump -nn tcp
```

## Resource: State and connection exhaustion Example, Firewall can handle 10,000 simultaneous connections, and attacker sends 20,000
```
# netstat -n I awk '{print $6}' I sort I uniq -c sort -nr I head
```
## Application: Layer 7 attacks Example, HTTP GET flood, for a large image file.
```
# tshark -c 10000 -T fields -e http.host| uniq -c | sort -r | head -n 10 so rt |
# tshark -r capture6 -T fields -e http.request.full\_uri I sort I uniq -c I sort -r I head -n 10c
# tcpdump -n 'tcp[32:4] = 0x47455420' I cut -f 7- -d II• II
```
## Example, look for excessive file requests, GIF, ZIP,JPEG, PDF, PNG.
```
# tshark -Y "http contains 11ff :d811 11 11 "http contains 11GIF89a11 " I I "http contains 11\x50\x4B\x03\x0411 11 11 "http contains\xff\xd8 11 11 11 "http contains 11%PDF11 11 I I "http contains "\x89\x50\x4E\x47""
```
## Example, Look for web application 'user-agent' pattern of abuse.
```
# tcpdump -c 1000 -Ann I grep -Ei 'user-agent' sort I uniq -c I sort -nr I head -10
```
## Example, show HTTP Header of requested resources.
```
# tcpdump -i en0 -A -s 500 I grep -i refer
```
## Sniff HTTP Headers for signs of repeat abuse:
```
# tcpdump -s 1024 -l -A dst <EXAMPLE.COM>
```
# Poison: Layer 2 attacks
## Example, ARP poison, race condition DNS, DHCP
```
# tcpdump 'arp or icmp'
# tcpdump -tnr <SAMPLE TRAFFIC FILE>.pcap ARP lawk -F ',' '{print $1"."$2","$3","$4}' I sort I uniq -c sort -n I tail
# tshark -r <SAMPLE TRAFFIC FILE>.pcap -q -z io,phsl grep arp.duplicate-address-detected
```