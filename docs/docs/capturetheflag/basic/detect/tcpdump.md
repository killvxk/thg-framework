# View ASCII (-A) or HEX (-X) traffic:
```
tcpdump -A
tcpdump -X
```
## View traffic with timestamps and don't convert addresses and be verbose:
```
tcpdump -tttt -n -vv
```

## Find top talkers after 1000 packets (PotentialDDoS):
```
tcpdump -nn -c 1000 jawk '{print $3}' I cut -d. -fl-4 I sort -n I uniq -c I sort -nr
```

## Capture traffic on any interface from a target host and specific port and output to a file:
```
tcpdump -w <FILENAME>,pcap -i any dst <TARGET IPADDRESS> and port 80
```

## View traffic only between two hosts:
```
tcpdump host 10.0.0.1 && host 10.0.0.2
```
## View all traffic except from a net or a host:
```
tcpdump not net 10.10 && not host 192.168.1,2
```
## View host and either of two other hosts:
```
tcpdump host 10,10,10.10 && \(10,10.10.20 or 10,10,10,30\)
```

## Save pcap file on rotating size:
```
tcpdump -n -s65535 -c 1000 -w '%host_%Y-%m­%d_%H:%M:%S.pcap'
```

## Save pcap file to a remote host:
```
tcpdump -w - I ssh <REMOTE HOST ADDRESS> -p 50005 "cat - > /tmp/remotecapture.pcap"
```
## Grab traffic that contains the word pass:
```
tcpdump -n -A -s0 I grep pass
```

## Grab many clear text protocol passwords:
```
tcpdump -n -A -s0 port http or port ftp or port smtp or port imap or port pop3 I egrep -i 'pass=lpwd=llog=llogin=luser=lusername=lpw=lpassw=IP asswd=lpassword=lpass: I user: lusername: I password: I login: I pass I user ' --color=auto --line-buffered -B20
```

## Get throughput
```
tcpdump -w - lpv -bert >/dev/null
```

## Filter out ipv6 traffic:
```
tcpdump not ip6
```

## Filer out ipv4 traffic:
```
tcpdump ip6
```

## Script to capture multiple interface tcpdumps to files rotating every hour:
```
#!/bin/bash
tcpdump -pni any -s65535 -G 3600 -w any%Y-%m­%d_%H:%M:%S.pcap
```

## Script to move multiple tcpdump files to alternate location:
```
#!/bin/bash
while true; do
sleep 1;
rsync -azvr -progress <USER NAME>@<IP
ADDRESS>:<TRAFFIC DIRECTORY>/, <DESTINATION
DIRECTORY/.
done
```

## Look for suspicious and self-signed SSL certificates:
```
tcpdump -s 1500 -A '(tcp[((tcp[12:1] & 0xf0) >> 2)+5:1] = 0x01) and (tcp[((tcp[12:1] & 0xf0) >> 2) : 1] : 0x16) I
```

## Get SSL Certificate:
```
openssl s_client -connect <URL>:443
openssl s_client -connect <SITE>:443 </dev/null 2>/dev/null I sed -ne '/-BEGIN CERTIFICATE-/,/-END CERTIFICATE-Ip' > <CERT>.pem
```

## Examine and verify the certificate and check for Self-Signed:
```
openssl x509 -text -in <CERT>.pem
openssl x509 -in <CERT>,pem -noout -issuer -subject -startdate -enddate -fingerprint
openssl verify <CERT>.pem
```

## Extract Certificate Server Name:
```
tshark -nr <PCAP FILE NAME> -Y "ssl. handshake. ciphersuites" -Vx I grep "ServerName:" I sort I uniq -c I sort -r
```

## Extract Certificate info for analysis:
```
ssldump -Nr <FILE NAME>.pcap I awk 'BEGIN {c=0;}{ if ($0 � /A[ ]+Certificate$/) {c=l; print"========================================";} if($0 !�/A +/) {c=0;} if (c==l) print $0; }'
```