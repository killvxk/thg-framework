## Get list of network interfaces:
```
tshark -D
```
## Listen on multiple network interfaces:
```
tshark -i ethl -i eth2 -i eth3
```
## Save to pcap and disable name resolution:
```
tshark -nn -w <FILE NAME>,pcap
```
## Get absolute date and time stamp:
```
tshark -t a
```
## Get arp or icmp traffic:
```
tshark arp or icmp
```
## Capture traffic between to [hosts] and/or [nets]:
```
tshark "host <HOST l> && host <HOST 2>"
tshark -n "net <NET 1> && net <NET 2>"
```
## Filter just host and IPs (or not your IP):
```
tshark -r <FILE NAME>,pcap -q -z hosts,ipv4
tshark not host <YOUR IP ADDRESS>
```
## Not ARP and not UDP:
```
tshark not arp and not (udp.port -- 53)
```
## Replay a pcap file:
```
tshark -r <FILE NAME>.pcap
```
## Replay a pcap and just grab hosts and IPs:
```
tshark -r <FILE NAME>.pcap -q -z hosts
```
## Setup a capture session(duration=60sec):
```
tshark -n -a files:10 -a filesize:100 -a duration:60 -w <FILE NAME>,pcap
```

## Grab src/dst IPs only:
```
tshark -n -e ip.src -e ip.dst -T fields -E separator=, -Rip
```

## Grab IP of src DNS and DNS query:
```
tshark -n -e ip.src -e dns,qry.name -E separator=';' -T fields port 53
```
## Grab HTTP URL host and request:
```
tshark -R http.request -T fields -E separator=';' -e http.host -e http.request.uri
```
## Grab just HTTP host requests:
```
tshark -n -R http.request -T fields -e http.host
```
## Grab top talkers by IP dst:
```
tshark -n -c 150 I awk '{print $4}' I sort -n Iuniq -c I sort -nr
```
## Grab top stats of protocols:
```
tshark -q -z io,phs -r <FILE NAME>.pcap
tshark -r <PCAP FILE>,cap -R http.request -T fields -e http.host -e http.request.uri lsed -e 'sf?,*$//' I sed -e 's#"(,*)t(,*)$#http://l2#' I sort I uniq -c I sort -rn I head
tshark -n -c 100 -e ip.src -R "dns.flags.responseeq 1" -T fields po rt 53
tshark -n -e http.request.uri -R http.request -T fields I grep exe
tshark -n -c 1000 -e http.host -R http.request -T fields port 80 I sort I uniq -c I sort -r
```
