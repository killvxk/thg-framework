## Authentication logs in Ubuntu:
```
tail /var/log/auth. log
grep -i "fail" /var/log/auth. log
```
## User login logs in Ubuntu:
```
tail /var/
```
## Look at samba activity:
```
grep -i samba /var/log/syslog
```
## Look at cron activity:
```
grep -i cron /var/log/syslog
```
## Look at sudo activity:
```
grep -i sudo /var/log/auth. log
```
## Look in Apache Logs for 404 errors:
```
grep 404 <LOG FILE NAME> I grep -v -E "favicon. ico I robots. txt"
```

## Look at Apache Logs for files requested:
```
head access_log I awk '{print $7}'
```
## Monitor for new created files every Smin:
```
watch -n 300 -d ls -lR /<WEB DIRECTORY>
```
## Look where traffic is coming from:
```
cat <LOG FILE NAME> I fgrep -v <YOUR DOMAIN> I cut -d\" -f4 I grep -v ""-
```
## Monitor for TCP connections every 5 seconds:
```
netstat -ac 5 I grep tcp
```
## Install audit framework and review syscalls/events:
```
apt-get install auditd
auditctl -a exit,always -5 execve
ausearch -m execve
```
## Get audit report summary:
```
aureport
```

