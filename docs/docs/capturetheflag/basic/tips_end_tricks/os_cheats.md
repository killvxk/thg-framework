# WINDOWS
## Pipe output to clipboard:
C:\> some_command.exe
## I clip Output clip to file: (Requires PowerShell 5)
PS C:\> Get-Clipboard> clip.txt
## Add time stamps into log file:
C:\> echo %DATE% %TIME%>> <TXT LOG>,txt
## Add/Modify registry value remotely:
C:\> reg add \\<REMOTE COMPUTERNAME>\HKLM\Software\<REG KEY INFO>Get registry value remotely:
C:\> reg query \\<REMOTE COMPUTERNAME>\HKLM\Software\<REG KEY INFO>
## Test to see if Registry Path exists:
PS C:\> Test-Path "HKCU:\Software\Microsoft\<HIVE>"
## Copy files remotely:
C:\> robocopy C:\<SOURCE SHARED FOLDER>\\<DESTINATION COMPUTER>\<DESTINATION FOLDER> /E
## Check to see if certain file extensions are in adirectory:
PS C:\> Test-Path C:\Scripts\Archive\* -include *·PSl, *,VbS
## Show contents of a file:
C:\> type <FILE NAME>

## Combine contents of multiple files:
C:\> type <FILE NAME 1> <FILE NAME 2> <FILE NAME 3>> <NEW FILE NAME>
## Desktops, allows multiple Desktop Screens:
Ref. https://technet.microsoft.com/enus/sysinternals/cc817881

## Run live option:
C:\> "%ProgramFiles%\Internet Explorer\iexplore.exe "https://live.sysinternals.com/desktops.exe
## Remote mounting, Read and Read/Write:
C:\> net share MyShare_R=c:\<READ ONLY FOLDER>/GRANT:EVERYONE,READ
C:\> net share MyShare_RW=c:\<READ/WRITE FOLDER>/GRANT:EVERYONE,FULL
## Remote task execution using PSEXEC:
Ref. https://technet.microsoft.com/enus/sysinternals/psexec.aspx

C:\> psexec.exe \\<TARGET IP ADDRESS> -u <USER NAME>-p <PASSWORD> /C C:\<PROGRAM>.exe
C:\> psexec @(:\<TARGET FILE LIST>.txt -u <ADMINLEVEL USER NAME> -p <PASSWORD> C:\<PROGRAM>,exe >>
C:\<OUTPUT FILE NAME>,txt
C:\> psexec.exe @(:\<TARGET FILE LIST>.csv -u<DOMAIN NAME>\<USER NAME> -p <PASSWORD> /c
C:\<PROGRAM>.exe
## Remote task execution and send output to share:
C:\> wmic /node:ComputerName process call createucmd,exe /c netstat -an > \\<REMOTE SHARE>\<OUTPUTFILE NAME>,txtn

## Compare two files for changes:
PS C:\> Compare-Object (Get-Content ,<LOG FILE NAMEl>, log) -DifferenceObject (Get-Content .<LOG FILENAME 2>,log)
## Remote task execution using PowerShell:
PS C:\> Invoke-Command -<COMPUTER NAME> {<PSCOMMAND>}
## PowerShell Command Help:
PS C:\> Get-Help <PS COMMAND> -full

# LINUX
## Analyze traffic remotely over ssh:
```
# ssh root@<REMOTE IP ADDRESS OF HOST TO SNIFF>tcpdump -i any -U -s 0 -w - 'not port 22'
```
## Manually add note/data to syslog:
# logger usomething important to note in Log"
# dmesg I grep <COMMENT>
## Simple read only mounting:
# mount -o ro /dev/<YOUR FOLDER OR DRIVE> /mnt
## Mounting remotely over SSH:
# apt-get install sshfs
# adduser <USER NAME> fuse
## Log out and log back in.
mkdir �/<WHERE TO MOUNT LOCALLY>
# sshfs <REMOTE USER NAME>@<REMOTE HOST>:/<REMOTEPATH> �/<WHERE TO MOUNT LOCALLY>

## Creating SMB share in Linux:
# useradd -m <NEW USER>
# passwd <NEW USER>
# smbpasswd -a <NEW USER>
# echo [Share] >> /etc/samba/smb.conf
# echo /<PATH OF FOLDER TO SHARE> >>/etc/samba/smb.conf
# echo available = yes >> /etc/samba/smb.conf
# echo valid users = <NEW USER> >>/etc/samba/smb.conf
# echo read only = no >> /etc/samba/smb.conf
# echo browsable = yes >> /etc/samba/smb.conf
# echo public = yes >> /etc/samba/smb.conf
# echo writable = yes >> /etc/samba/smb.conf
# service smbd restart
## Visit share from remote system:
smb:\\<IP ADDRESS OF LINUX SMB SHARE>
## Copy files to remote system:
scp <FILE NAME> <USER NAME>@<DESTINATION IPADDRESS>:/<REMOTE FOLDER>
## Mount and SMB share to remote system:
# mount -t smbfs -o username=<USER NAME> //<SERVERNAME OR IP ADDRESS>/<SHARE NAME> /mnt/<MOUNT POINT>/

## Monitor a website or file is still up/there:

#while :; do curl -sSr http://<URL> I head -n 1;
sleep 60; done

