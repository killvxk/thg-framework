# linux

# NETWORK DISCOVERY

## Net view scan:
```
smbtree -b
smbtree -D
smbtree -5
```

## View open 5MB shares:
```
smbclient -L <HOST NAME>
smbstatus
```
## Basic ping scan:
```
for ip in $(seq 1 254); do ping -c 1 192.168.1.$ip>/dev/null; [ $? -eq 0 ] && echo "192.168.1. $ip UP" 11 : ; done
```

# DHCP

## View DHCP lease logs:
```
Red Hat 3:
cat /var/lib/dhcpd/dhcpd. leases

Ubuntu:
grep -Ei 'dhcp' /var/log/syslog.1
```
## Ubuntu DHCP logs:
```
tail -f dhcpd. log
```
# DNS
## Start DNS logging:
```
rndc querylog
```

## View DNS logs:
```
tail -f /var/log/messages I grep named
```

#HASHING

## Hash all executable files in these specified locations:
```
find /<PATHNAME TO ENUMERATE> -type f -exec mdSsum {} >> mdSsums.txt \;
mdSdeep -rs /> mdSsums.txt
```
# NETBIOS

## Basic nbtstat scan:
```
nbtscan <IP ADDRESS OR RANGE>
```

# PASSWORDS

## Password and username guessing or checks:
```
while read line; do username=$line; while readline; do smbclient -L <TARGET IP ADDRESS> -U $username%$line -g -d 0; echo $username:$line;done<<PASSWORDS>.txt; done<<USER NAMES>,txt
```
