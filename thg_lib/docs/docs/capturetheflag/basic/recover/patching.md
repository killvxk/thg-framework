# WINDOWS

## Single Hotfix update for Windows 7 or higher:
```
C:\> wusa.exe C:\<PATH TO HOTFIX>\Windows6.0-KB934307-x86.msu
```
## Set of single hotfix updates for pre Windows 7 by running a batch script:
```
@echo off
setlocal
set PATHTOFIXES=E:\hotfix
%PATHTOFIXES%\Q123456_w2k_sp4_x86.exe /2 /M
%PATHTOFIXES%\Ql23321_w2k_sp4_x86.exe /2 /M
%PATHTOFIXES%\Q123789_w2k_sp4_x86.exe /2 /M
```
## To check and update Windows 7 or higher:
```
C:\> wuauclt.exe /detectnow /updatenow
```
# LINUX

## Ubuntu: Fetch list of available updates:
```
apt-get update
```
## Strictly upgrade the current packages:
```
apt-get upgrade
```
## Install updates (new ones):
```
apt-get dist-upgrade
```

## Red Hat Enterprise Linux 2.1,3,4:
```
up2date
```
## To update non-interactively:
```
up2date-nox --update
```
## To install a specific package:
```
up2date <PACKAGE NAME>
```
## To update a specific package:
```
up2date -u <PACKAGE NAME>
```
## Red Hat Enterprise Linux 5:
```
pup
```
## Red Hat Enterprise Linux 6:
```
yum update
```
## To list a specific installed package:
```
yum list installed <PACKAGE NAME>
```
## To install a specific package:
```
yum install <PACKAGE NAME>
```
## To update a specific package:
```
yum update <PACKAGE NAME>
```
## Kali:
```
apt-get update && apt-get upgrade
```
