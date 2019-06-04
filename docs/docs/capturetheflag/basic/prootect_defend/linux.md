# DISABLE/STOP SERVICES

## Services information:
```
service --status-all
ps -ef
ps -aux
```

## Get a list of upstart jobs:
```
initctl list
```
## Example of start, stop, restarting a service in
```
Ubuntu:
/etc/init,d/apache2 start
/etc/init.d/apache2 restart
/etc/init.d/apache2 stop (stops only until reboot)
service mysql start
service mysql restart
service mysql stop (stops only until reboot)
```
## List all Upstart services:
```
ls /etc/init/*,conf
```
## Show if a program is managed by upstart and the process ID:
```
status ssh
```
## If not managed by upstart:
```
update-rc.d apache2 disable
service apache2 stop
```

# HOST SYSTEM FIREWALLS

## Export existing iptables firewall rules:
```
iptables-save > firewall.out
```
## Edit firewall rules and chains in firewall.out and save the file:
```
nano firewall.out
```
## Apply iptables:
```
iptables-restore < firewall.out
```
## Example iptables commands (IP, IP Range, Port Blocks):
```
iptables -A INPUT -s 10.10.10.10 -j DROP
iptables -A INPUT -s 10,10.10.0/24 -j DROP
iptables -A INPUT -p tcp --dport ssh 10.10.10.10 -j DROP
iptables -A INPUT -p tcp --dport ssh -j DROP
```
## Block all connections:
```
iptables-policy INPUT DROP
iptables-policy OUTPUT DROP
iptables-policy FORWARD DROP
```
## Log all denied iptables rules:
```
iptables -I INPUT 5 -m limit --limit 5/min -j LOG --log-prefix "iptables denied: " --log-level 7
```
## Save all current iptables rules:
```
Ubuntu:
 /etc/init.d/iptables save
 /sbin/service iptables save

RedHat / CentOS:
 /etc/init.d/iptables save
 /sbin/iptables-save
````

## List all current iptables rules:
```
iptables -L
```
## Flush all current iptables rules:
```
iptables -F
```
## Start/Stop iptables service:
```
service iptables start
service iptables stop
```
## Start/Stop ufw service:
```
ufw enable
ufw disable
```
## Start/Stop ufw logging:
```
ufw logging on
ufw logging off
```
## Backup all current ufw rules:
```
cp /lib/ufw/{user.rules,user6.rules} /<BACKUPLOCATION>
cp /lib/ufw/{user.rules,user6.rules} ./
```
## Example uncomplicated firewall (ufw) Commands (IP,IP range, Port blocks):
```
ufw status verbose
ufw delete <RULE#>
ufw allow for <IP ADDRESS>
ufw allow all 80/tcp
ufw allow all ssh
ufw deny from <BAD IP ADDRESS> proto udp to any port 443
```

# PASSWORDS
## Change password:
```
passwd (For current user)
passwd bob (For user Bob)
sudo su passwd (For root)
```
# HOST FILE
## Add new malicious domain to hosts file, and route to localhost:
```
echo 127.0.0,1 <MALICIOUS DOMAIN> >> /etc/hosts
```
## Check if hosts file is working, by sending ping to 127.0.0.1:
```
ping -c 1 <MALICIOUS DOMAIN>
```
## Ubuntu/Debian DNS cache flush:
```
/etc/init.d/dns-clean start
```
## Flush nscd DNS cache four ways:
```
/etc/init.d/nscd restart
service nscd restart
service nscd reload
nscd -i hosts
````

## Flush dnsmasq DNS cache:
```
/etc/init.d/dnsmasq restart
```
# WHITELIST

## Use a Proxy Auto Config(PAC) file to create bad URLor IP List:
```
function FindProxyForURL(url, host) {
// Send bad DNS name to the proxy
if (dnsDomainis(host, ",badsite.com"))
return "PROXY http:11127.0.0.1:8080";
// Send bad IPs to the proxy
if (isinNet(myipAddress(), "222.222.222.222",
"255.255.255.0"))
return "PROXY http:11127.0.0.1:8080";
// All other traffic bypass proxy
return "DIRECT";
}
```

# IPSEC
## Allow firewall to pass IPSEC traffic:
```
iptables -A INPUT -p esp -j ACCEPT
iptables -A INPUT -p ah -j ACCEPT
iptables -A INPUT -p udp --dport 500 -j ACCEPT
iptables -A INPUT -p udp --dport 4500 -j ACCEPT
```

# Pass IPSEC traffic:
## Step 1:
```
Install Racoon utility on <HOSTl IP ADDRESS>and <HOST2 IP ADDRESS> to enable IPSEC tunnel inUbuntu.

apt-get install racoon
```
## Step 2:
```
Choose direct then edit letclipsectools.conf
on <HOSTl IP ADDRESS> and <HOST2 IPADDRESS>.

flush;
spdflush;
spdadd <HOSTl IP ADDRESS> <HOST2 IP ADDRESS> any -P out ipsec
    esp/transport//require;
s pdadd <HOST2 IP ADDRESS> <HOSTl IP ADDRESS> any -P
in ipsec

esp/transport//require;
```
## Step 3:
```
Edit /etc/racoon/racoon.conf on <HOSTl IP
ADDRESS> and <HOST2 IP ADDRESS>,
log notify;
path pre_shared_key "/etc/racoon/psk.txt";
path certificate "/etc/racoon/certs";
remote anonymous {
exchange_mode main,aggressive;
proposal {
encryption_algorithm aes_256;
hash_algorithm sha256;
authentication_method
pre_shared_key;
dh_group modp1024;
}
generate_policy off;
}
sainfo anonymous{
}
```

## Step 4:
```
Add preshared key to both hosts.On HOSTl:
 echo <HOST2 IP ADDRESS> <PRESHARED PASSWORD> >>/etc/racoon/psk.txt
On HOST2:
 echo <HOSTl IP ADDRESS> <PRESHARED PASSWORD> >>/etc/racoon/psk.txt
```
## Step 5:
```
Restart service on both systems.
 service setkey restart
Check security associations, configuration and
polices:
 setkey -D
 setkey -DP
```