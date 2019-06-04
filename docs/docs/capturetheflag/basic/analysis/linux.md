# SYSTEM INFORMATION
```
uname -a
uptime
timedatectl
mount
```

# USER INFORMATION

## View logged in users:
```
w
```

## Show if a user has ever logged in remotely:
```
lastlog
last
```

## View failed logins:
```
faillog -a
```

## View local user accounts:
```
cat /etc/passwd
cat/etc/shadow
```

## View local groups:
```
cat/etc/group
```
## View sudo access:
```
cat /etc/sudoers
```
## View accounts with UID 0:
```
awk -F: '($3 == "0") {p rint}' /etc/passwd
egrep ':0+' /etc/passwd
```

## View root authorized SSH key authentications:
```
cat /root/.ssh/authorized_keys
```

## List of files opened by user:
```
lsof -u <USER NAME>
```

## View the root user bash history:
```
cat /root/,bash_history
```

# NETWORK INFORMATION
## View network interfaces:
```
ifconfig
```
## View network connections:
```
netstat -antup
netstat -plantux
```

## View listening ports:
```
netstat -nap
```
## View routes:
```
route
```

## View arp table:
```
arp -a
```

## List of processes listening on ports:
```
lsof -i
```

# SERVICE INFORMATION

## View processes:
```
ps -aux
```
## List of load modules:
```
lsmod
```

## List of open files:
```
lsof
```

## List of open files, using the network:
```
lsof -nPi I cut -f 1 -d " "I uniq I tail -n +2
```

## List of open files on specific process:
```
lsof -c <SERVICE NAME>

```

## Get all open files of a specific process ID:
```
lsof -p <PID>
```

## List of unlinked processes running:
```
lsof +Ll
```

## Get path of suspicious process PID:
```
ls -al /proc/<PID>/exe
```

## Save file for further malware binary analysis:
```
cp /proc/<PID>/exe >/<SUSPICIOUS FILE NAME TO SAVE>,elf Monitor logs in real-time:
less +F /var/log/messages
```
## List services:
```
chkconfig --list
```

# POLICY, PATCH AND SETTINGS INFORMATION

## View pam.d files:
```
cat /etc/pam.d/common*
```

# AUTORUN AND AUTOLOAD INFORMATION:
## List cron jobs:
```
crontab -l
```
## List cron jobs by root and other UID 0 accounts:
```
crontab -u root -l
```
## Review for unusual cron jobs:
```
cat /etc/crontab
ls /etc/cron,*
```
# LOGS

## View root user command history:
```
cat /root/,*history
```
## View last logins:
```
last
```

# FILES, DRIVES AND SHARES INFORMATION
## View disk space:
```
df -ah
```
## View directory listing for /etc/init.d:
```
ls -la /etc/init.d
```
## Get more info for a file:
```
stat -x <FILE NAME>
```
## Identify file type:
```
file <FILE NAME>
```
## Look for immutable files:
```
lsatt r -R / I g rep 11 \ -i11
```

## View directory listing for /root:
```
ls -la /root
```
## Look for files recently modified in current directory:
```
ls -alt I head
```

## Look for world writable files:
```
#find/ -xdev -type d\( -perm -0002 -a ! -perm -1000 \) -print
```
## Look for recent created files, in this case newer than Jan 02, 2017:
```
find/ -n ewermt 2017-01-02q
```
## List all files and attributes:
```
#find/ -printf 11%m;%Ax;%AT;%Tx;%TT;%Cx;%CT;%U;%G;%s;%p\n"
```
## Look at files in directory by most recent timestamp:(Could be tampered)
```
ls -alt /<DIRECTORY>! head
```

## Get full file information:
```
# stat /<FILE PATH>/<SUSPICIOUS FILE NAME>
```

## Review file type:
```
# file /<FILE PATH>/<SUSPICIOUS FILE NAME>
```

## Check for rootkits or signs of compromise:
## Run unix-privsec-check tool:
```
# wget
https://raw.githubusercontent.com/pentestmonkey/unix-privesc-check/l_x/unix-privesc-check
# ./unix-privesc-check > output.txt
```

## Run chkrootkit:
```
apt-get install chkrootkit
chkrootkit
```
## Run rkhunter:
```
apt-get install rkhunter
rkhunter --update
rkhunter -check
```
## Run tiger:
```
apt-get install tiger
tiger
less /var/log/tiger/security.report,*
```
## Run lynis:
```
apt-get install lynis
lynis audit system
more /var/logs/lynis. log
```
## Run Linux Malware Detect (LMD):
```
wget http://www.rfxn.com/downloads/maldetectcurrent.tar.gz

tar xfz maldetect-current.tar.gz
cd maldetect-*
./install.sh
=> Get LMD updates:
maldet -u
Run LMD scan on directory:
maldet -a /<DIRECTORY>
```