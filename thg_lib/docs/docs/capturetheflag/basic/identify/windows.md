# NETWORK DISCOVERY
## Basic network discovery:
```
C:\> net view /all
C:\> net view \\<HOST NAME>
```

## Basic ping scan and write output to file:
```
C:\> for /L %I in (1,1,254) do ping -w 30 -n 1 192.168. l.%I I find "Reply" >> <OUTPUT FILENAME>.txt
```

# DHCP

## Enable DHCP server logging:
```
C:\> reg add HKLM\System\CurrentControlSet\Services\DhcpServer\Parameters /v ActivityLogFlag /t REG_DWORD /d 1
```

## Default Location Windows 2003/2008/2012:
```
C:\> %windir%\System32\Dhcp
```

# DNS
## Default location Windows 2003:
```
C:\> %SystemRoot%\System32\Dns
```
## Default location Windows 2008:
```
C:\> %SystemRoot%\System32\Winevt\Logs\DNSServer. evtx
```
## Default location of enhanced DNS Windows 2012 R2:
```
C:\> %SystemRoot%\System32\Winevt\Logs\MicrosoftWindows-DNSServer%4Analytical.etl
```

## ![ref](https://technet.microsoft.com/enus/library/cc940779.aspx)

## Enable DNS Logging:
```
C:\> DNSCmd <DNS SERVER NAME> /config /logLevel0x8100F331
```

## Set log location:
```
C:\> DNSCmd <DNS SERVER NAME> /config /LogFilePath<PATH TO LOG FILE>
```

## Set size of log file:
```
C:\> DNSCmd <DNS SERVER NAME> /config/logfilemaxsize 0xffffffff
```

# HASHING

## File Checksum Integrity Verifier (FCIV):

## ![Ref](http://support2.microsoft.com/kb/841290)

## Hash a file:
```
C:\> fciv.exe <FILE TO HASH>
```

## Hash all files on C:\ into a database file:
```
C:\> fciv.exe c:\ -r -mdS -xml <FILE NAME>.xml
```

## List all hashed files:
```
C:\> fciv.exe -list -shal -xml <FILE NAME>.xml
```

## Verify previous hashes in db with file system:
```
C:\> fciv.exe -v -shal -xml <FILE NAME>.xml

Note: May be possible to create a master db and
compare to all systems from a cmd line. Fast
baseline and difference.
```

![Ref](https://technet.microsoft.com/enus/library/dn520872.aspx)
```
PS C:\> Get-FileHash <FILE TO HASH> I Format-List
PS C:\> Get-FileHash -algorithm md5 <FILE TO HASH>
C:\> certutil -hashfile <FILE TO HASH> SHAl
C:\> certutil -hashfile <FILE TO HASH> MD5
```

# NETBIOS

## Basic nbtstat scan:
```
C:\> nbtstat -A <IP ADDRESS>
```

## Cached NetBIOS info on localhost:
```
C:\> nbtstat -c
```
# Script loop scan:
```
C:\> for /L %I in (1,1,254) do nbstat -An 192.168.l.%I
```

## USER ACTIVITY
![Ref](https://technet.microsoft.com/enus/sysinternals/psloggedon.aspx)

## Get users logged on:
```
C:\> psloggedon \\computername
```
## Script loop scan:
```
C:\> for /L %i in (1,1,254) do psloggedon\\192.168.l.%i >> C:\users_output.txt
```

# PASSWORDS

## Password guessing or checks:
```
# for /f %i in (<PASSWORD FILE NAME>.txt) do @echo %i & net use \\<TARGET IP ADDRESS> %i /u:<USERNAME> 2>nul && pause
# for /f %i in (<USER NAME FILE>.txt) do @(for /f %j
in (<PASSWORD FILE NAME>.txt) do @echo %i:%j & @net
use \\<TARGET IP ADDRESS> %j /u:%i 2>nul &&
echo %i:%j >> success.txt && net use \\<IP ADDRESS>/del)
MICROSOFT BASELINE SECURITY ANALYZER (MBSA)
```

## Basic scan of a target IP address:
```
C:\> mbsacli.exe /target <TARGET IP ADDRESS> /n os+iis+sql+password
```
## Basic scan of a target IP range:
```
C:\> mbsacli.exe /r <IP ADDRESS RANGE> /n os+iis+sql+password
```

## Basic scan of a target domain:
```
C:\> mbsacli.exe /d <TARGET DOMAIN> /n os+iis+sql+password
```
## Basic scan of a target computer names in text file:
```
C:\> mbsacli.exe /listfile <LISTNAME OF COMPUTERNAMES>.txt /n os+iis+sql+password
```
## ACTIVE DIRECTORY INVENTORY List all OUs:
```
C:\> dsquery ou DC=<DOMAIN>,DC=<DOMAIN EXTENSION>
```
## List of workstations in the domain:
```
C:\> netdom query WORKSTATION
```

## List of servers in the domain:
```
C:\> netdom query SERVER
```
## List of domain controllers:
```
C:\> netdom query DC
```
## List of organizational units under which the specified user can create a machine object:
```
C:\> netdom query OU
```
## List of primary domain controller:
```
C:\> netdom query PDC
```
## List the domain trusts:
```
C:\> netdom query TRUST
```
## Query the domain for the current list of FSMO owners
```
C:\> netdom query FSMO
```
## List all computers from Active Directory:
```
C:\> dsquery COMPUTER "OU=servers,DC=<DOMAINNAME>,DC=<DOMAIN EXTENSION>" -o rdn -limit 0 >
C:\machines.txt
```
## List user accounts inactive longer than 3 weeks:
```
C:\> dsquery user domainroot -inactive 3
```
## Find anything (or user) created on date in UTC using timestamp format YYYYMMDDHHMMSS.sZ:
```
C:\> dsquery * -filter"(whenCreated>=20101022083730,0Z)"
C:\> dsquery * -filter"((whenCreated>=20101022083730.0Z)&(objectClass=user))II
```

## Alt option:
```
C:\> ldifde -d ou=<OU NAME>,dC=<DOMAINNAME>,dc=<DOMAIN EXTENSION> -l whencreated,whenchanged -p onelevel -r "(ObjectCategory=user)" -f <OUTPUT FILENAME>
```
## The last logon timestamp format in UTC:YYYYMMDDHHMMSS Alt option:
```
C:\> dsquery * dc=<DOMAIN NAME>,dc=<DOMAINEXTENSION> -filter "(&(objectCategory=Person)(objectClass=User)(whenCreated>=20151001000000.0Z))"
```

## Alt option:
```
C:\> adfind -csv -b dc=<DOMAIN NAME>,dc=<DOMAINEXTENSION> -f "(&(objectCategory=Person)(objectClass=User)(whenCreated>=20151001000000.0Z))"
```
## Using PowerShell, dump new Active Directory accounts in last 90 Days:
```
PS C:\> import-module activedirectory
PS C:\> Get-QADUser -CreatedAfter (GetDate).AddDays(-90)
PS C:\> Get-ADUser -Filter * -Properties whenCreatedI Where-Object {$_.whenCreated -ge ((GetDate).AddDays(-90)).Date}
```


