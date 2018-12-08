# WINDOWS
## Backup GPO Audit Policy to backup file:
```
C:\> auditpol /backup /file:C\auditpolicy.csv
```
## Restore GPO Audit Policy from backup file:
```
C:\> auditpol /restore /file:C:\auditpolicy.csv
```
## Backup All GPOs in domain and save to Path:
```
PS C:\> Backup-Gpo -All -Path \\<SERVER>\<PATH TOBACKUPS>
```
## Restore All GPOs in domain and save to Path:
```
PS C:\> Restore-GPO -All -Domain <INSERT DOMAINNAME> -Path \\Serverl\GpoBackups
```
## Start Volume Shadow Service:
```
C:\> net start VSS
```
## List all shadow files and storage:
```
C:\> vssadmin List ShadowStorage
```
## List all shadow files:
```
C:\> vssadmin List Shadows
```
## Browse Shadow Copy for files/folders:
```
C:\> mklink /d c:\<CREATE FOLDER>\<PROVIDE FOLDERNAME BUT DO NOT CREATE>\\?\GLOBALROOT\Device\HarddiskVolumeShadowCopyl\
```
## Revert back to a selected shadow file on Windows Server and Windows 8:
```
C:\> vssadmin revert shadow /shadow={<SHADOW COPYID>} /ForceDismount
```
## List a files previous versions history using volrest.exe:
```
Ref. https://www.microsoft.com/enus/download/details.aspx?id=17657
C:\> "\Program Files (x86)\Windows ResourceKits\Tools\volrest.exe" "\\localhost\c$\<PATH TOFILE>\<FILE NAME>"
```
## Revert back to a selected previous file version or @GMT file name for specific previous version using volrest.exe:
```
C:\> subst Z: \\localhost\c$\$\<PATH TO FILE>
C:\> "\Program Files (x86)\Windows ResourceKits\Tools\volrest.exe" "\\localhost\c$\<PATH TOFILE>\<CURRENT FILE NAME OR @GMT FILE NAME FROM LISTCOMMAND ABOVE>" /R:Z:\
C:\> subst Z: /0
```
## Revert back a directory and subdirectory filesprevious version using volrest.exe:
```
C: \> "\Program Files (x86) \Windows ResourceKits\Tools\volrest.exe" \\localhost\c$\<PATH TOFOLDER\*·* /5 /r:\\localhost\c$\<PATH TO FOLDER>\
```
## Revert back to a selected shadow file on Windows Server and Windows 7 and 10 using wmic:
```
C:\> wmic shadowcopy call create Volume='C:\'
```
## Create a shadow copy of volume C on Windows 7 and 10 using PowerShell:
```
PS C:\> (gwmi -listwin32_shadowcopy).Create('C:\', 'ClientAccessible')
```
## Create a shadow copy of volume C on Windows Server 2003 and 2008:
```
C:\> vssadmin create shadow /for=c:
```
## Create restore point on Windows:
```
C:\> wmic.exe /Namespace:\\root\default Path
```
## SystemRestore Call CreateRestorePoint "%DATE%", 100, Start system restore points on Windows XP:
```
C:\> sc config srservice start= disabled
C:\> reg add "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\WindowsNT\CurrentVersion\SystemRestore" /v DisableSR /t REG_DWORD /d 1 /f
C:\> net stop srservice

```
## Stop system restore points on Windows XP:
```
C:\> sc config srservice start= Auto
C:\> net start srservice
C:\> reg add "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\WindowsNT\CurrentVersion\SystemRestore" /v DisableSR /t REG_DWORD /d 0 /f
```
## List of restore points:
```
PS C:\> Get-ComputerRestorePoint
```
## Restore from a specific restore point:
```
PS C:\> Restore-Computer -RestorePoint <RESTOREPOINT#> -Confirm
```
# LINUX
## Reset root password in single user mode:
## Step 1: Reboot system.
```
reboot -f
```
## Step 2: Press ESC at GRUB screen.
## Step 3: Select default entry and then 'e' for edit.
## Step 4: Scroll down until, you see a line that starts with linux, linux16 or linuxefi.
## Step 5: At end of that line leave a space and add without quote 'rw init=/bin/bash'
## Step 6: Press Ctrl-X to reboot.
## Step 7: After reboot, should be in single user modeand root, change password.
```
passwd
```
## Step 8: Reboot system.
```
# reboot -f
```
## Reinstall a package:
```
# apt-get install --reinstall <COMPROMISED PACKAGENAME>
```
## Reinstall all packages:
```
# apt-get install --reinstall $(dpkg --getselections lgrep -v deinstall)
```
# KILL MALWARE PROCESS

# WINDOWS
## Malware Removal:
```
Ref. http://www.gmer.net/
C:\> gmer.exe (GUI)
```
## Kill running malicious file:
```
C:\> gmer.exe -killfile
C:\WINDOWS\system32\drivers\<MALICIOUS FILENAME>.exe
```
## Kill running malicious file in PowerShell:
```
PS C:\> Stop-Process -Name <PROCESS NAME>
PS C:\> Stop-Process -ID <PID>
```
# LINUX
## Stop a malware process:
```
kill <MALICIOUS PID>
```
## Change the malware process from execution and move:
```
chmod -x /usr/sbin/<SUSPICIOUS FILE NAME>
mkdir /home/quarantine/
mv /usr/sbin/<SUSPICIOUS FILE NAME>/home/quarantine/
```