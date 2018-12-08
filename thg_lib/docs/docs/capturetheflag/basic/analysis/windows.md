# SYSTEM INFORMATION
```
C:\> echo %DATE% %TIME%
C:\> hostname
C:\> systeminfo
C:\> systeminfo I findstr /B /C:"OS Name" /C:"OSVersion"
C:\> wmic csproduct get name
C:\> wmic bios get serialnumber
C:\> wmic computersystem list brief

![Ref](https://technet.microsoft.com/enus/sysinternals/psinfo.aspx)
C:\> psinfo -accepteula -s -h -d
```
## USER INFORMATION
```
C:\> whoami
C:\> net users
C:\> net localgroup administrators
C:\> net group administrators
C:\> wmic rdtoggle list
C:\> wmic useraccount list
C:\> wmic group list
C:\> wmic netlogin getname, lastlogon,badpasswordcount
C:\> wmic netclient list brief
C:\> doskey /history> history.txt
```
## NETWORK INFORMATION
```
C:\> netstat -e
C:\> netstat -naob
C:\> netstat -nr
C:\> netstat -vb
C:\> nbtstat -s
C:\> route print
C:\> arp -a
C:\> ipconfig /displaydns
C:\> netsh winhttp show proxy
C:\> ipconfig /allcompartments /all
C:\> netsh wlan show interfaces
C:\> netsh wlan show all
C:\> reg query "HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Internet Settings\Connections\WinHttpSettings"
C:\> type %SYSTEMROOT%\system32\drivers\etc\hosts
C:\> wmic nicconfig getdescriptions,IPaddress,MACaddress
C:\> wmic netuse getname,username,connectiontype, localname
```
## SERVICE INFORMATION
```
C:\> at
C:\> tasklist
C:\> task list /SVC
C:\> tasklist /SVC /fi "imagename eq svchost.exe"
C:\> schtasks
C:\> net start
C:\> sc query
C:\> wmic service list brief
C:\> wmic service list conf ig
C:\> wmic process list brief
C:\> wmic process list status
C:\> wmic process list memory
C:\> wmic job list brief
```
## I findstr "Running"
```
PS C:\> Get-Service I Where-Object { $_.Status -eq"running" }
```
## List of all processes and then all loaded modules:
```
PS C:\> Get-Process !select modules!ForeachObject{$_.modules}
```
## POLICY, PATCH AND SETTINGS INFORMATION
```
C:\> set
C:\> gpresult /r
C:\> gpresult /z > <OUTPUT FILE NAME>.txt
C:\> gpresult /H report.html /F
C:\> wmic qfe
```
## List GPO software installed:
```
C:\> reg query uHKLM\Software\Microsoft\Windows\CurrentVersion\Group Policy\AppMgmt"
```
## AUTORUN AND AUTOLOAD INFORMATION Startup information:
```
C:\> wmic startup list full
C:\> wmic ntdomain list brief
```

## View directory contents of startup folder:
```
C:\> dir "%SystemDrive%\ProgramData\Microsoft\Windows\StartMenu\P rog rams\Sta rtup"
C:\> dir "%SystemDrive%\Documents and Settings\All Use rs\Sta rt Menu\Prog rams\Sta rtup"
C:\> dir %userprofile%\Start Menu\Programs\Startup
C:\> %ProgramFiles%\Startup\
C:\> dir C:\Windows\Start Menu\Programs\startup
C:\> dir "C:\Users\%username%\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup"
C:\> dir "C:\ProgramData\Microsoft\Windows\StartMenu\P rog rams\Sta rtup"
C:\> dir "%APPDATA%\Microsoft\Windows\StartMenu\Prog rams\Sta rtup"
C:\> dir "%ALLUSERSPROFILE%\Microsoft\Windows\StartMenu\Prog rams\Sta rtup"
C:\> dir "%ALLUSERSPROFILE%\StartMenu\P rog rams\Sta rtup"
C:\> type C:\Windows\winstart.bat
C:\> type %windir%\wininit.ini
C:\> type %windir%\win.ini
```
## View autoruns, hide Microsoft files:
![Ref](https://technet.microsoft.com/enus/sysinternals/bb963902.aspx)
```
C:\> autorunsc -accepteula -m
C:\> type C:\Autoexec.bat"
```
## Show all autorun files, export to csv and check withVirusTotal:
```
C:\> autorunsc.exe -accepteula -a -c -i -e -f -l -m -v
```

## HKEY_CLASSES_ROOT:
```
C:\> reg query HKCR\Comfile\Shell\Open\Command
C:\> reg query HKCR\Batfile\Shell\Open\Command
C:\> reg query HKCR\htafile\Shell\Open\Command
C:\> reg query HKCR\Exefile\Shell\Open\Command
C:\> reg query HKCR\Exefiles\Shell\Open\Command
C:\> reg query HKCR\piffile\shell\open\command
```
## HKEY_CURRENT_USERS:
```
C:\> reg query uHKCU\Control Panel\Desktop"
C:\> reg query HKCU\Software\Microsoft\Windows\CurrentVersion\Policies\Explorer\Run
C:\> reg query HKCU\Software\Microsoft\Windows\CurrentVersion\Run
C:\> reg query HKCU\Software\Microsoft\Windows\CurrentVersion\Runonce
C:\> reg query HKCU\Software\Microsoft\Windows\CurrentVersion\RunOnceEx
C:\> reg query HKCU\Software\Microsoft\Windows\CurrentVersion\RunServices
C:\> reg query HKCU\Software\Microsoft\Windows\CurrentVersion\RunServ ices Once
C:\> reg query HKCU\Software\Microsoft\Windows\CurrentVersion\Windows\Run
C:\> reg query HKCU\Software\Microsoft\Windows\CurrentVersion\Windows\Load
C:\> reg query HKCU\Software\Microsoft\Windows\CurrentVersion\Windows\Scripts
C:\> reg query HKCU\Software\Microsoft\WindowsNT\CurrentVersion\Windows /f run
C:\> reg query HKCU\Software\Microsoft\WindowsNT\CurrentVersion\Windows« /f load
C:\> reg query HKCU\Software\Microsoft\Windows\CurrentVersion\Policies\Explorer\Run
C:\> reg query HKCU\Software\Microsoft\Windows\CurrentVersion\Explorer\RecentDocs
C:\> reg query HKCU\Software\Microsoft\Windows\CurrentVersion\Explorer\ComDlg32\LastVisitedMRU
C:\> reg query HKCU\Software\Microsoft\Windows\CurrentVersion\Explorer\ComD1g32\0pen5aveMRU
C:\> reg query HKCU\Software\Microsoft\Windows\CurrentVersion\Explorer\ComDlg32\LastVisitedPidlMRU
C:\> reg query HKCU\Software\Microsoft\Windows\CurrentVersion\Explorer\ComD1g32\0pen5avePidlMRU /s
C:\> reg query HKCU\Software\Microsoft\Windows\CurrentVersion\Explorer\RunMRU
C:\> reg query HKCU\Software\Microsoft\Windows\CurrentVersion\Explorer\Shell Folders
C:\> reg query uHKCU\Software\Microsoft\Windows\CurrentVersion\Explorer\User Shell Folders"
C:\> reg query HKCU\Software\Microsoft\Windows\CurrentVersion\Applets\RegEdit /v LastKey
C:\> reg query HKCU\Software\Microsoft\InternetExp lo re r\ TypedURLs
C:\> reg query uHKCU\Software\Policies\Microsoft\Windows\ControlPanel \Desktop"
```
## HKEY_LOCAL_MACHINE:
```
C:\> reg query  HKLM\SOFTWARE\Mic rosoft\Act ive Setup\Installed Components /s
C:\> reg query  HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\explorer\User Shell Folders
C:\> reg query  HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\explorer\Shell Folders
C:\> reg query  HKLM\Software\Microsoft\Windows\CurrentVersion\explorer\ShellExecuteHooks
C:\> reg query  HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\Browser Helper Objects /s
C:\> reg query  HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\Explorer\Run
C:\> reg query  HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Run
C:\> reg query  HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Runonce
C:\> reg query  HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\RunOnceEx
C:\> reg query  HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\RunServices
C:\> reg query  HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\RunServicesOnce
C:\> reg query  HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Winlogon\Userinit
C:\> reg query  HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\shellServiceObjectDelayLoad
C:\> reg query  HKLM\SOFTWARE\Microsoft\WindowsNT\CurrentVersion\Schedule\TaskCache\Tasks /s
C:\> reg query  HKLM\SOFTWARE\Microsoft\WindowsNT\CurrentVersion\Windows
C:\> reg query  HKLM\SOFTWARE\Microsoft\WindowsNT\CurrentVersion\Windows /f Appinit_DLLs
C:\> reg query  HKLM\SOFTWARE\Microsoft\WindowsNT\CurrentVersion\Winlogon /f Shell
C:\> reg query  HKLM\SOFTWARE\Mic rosoft\WindowsNT\CurrentVersion\Winlogon /f Userinit
C:\> reg query  HKLM\SOFTWARE\Policies\Microsoft\Windows\Systern\Scripts
C:\> reg query  HKLM\SOFTWARE\Classes\batfile\shell\open\cornrnand
C:\> reg query  HKLM\SOFTWARE\Classes\cornfile\shell\open\cornrnand
C:\> reg query  HKLM\SOFTWARE\Classes\exefile\shell\open\command
C:\> reg query  HKLM\SOFTWARE\Classes\htafile\Shell\Open\Command
C:\> reg query  HKLM\SOFTWARE\Classes\piffile\shell\open\command
C:\> reg query  HKLM\SOFTWARE\Wow6432Node\Microsoft\Windows\CurrentVersion\Explorer\Browser Helper Objects /s
C:\> reg query  HKLM\SYSTEM\CurrentControlSet\Control\SessionManager
C:\> reg query  HKLM\SYSTEM\CurrentControlSet\Control\SessionManager\KnownDLLs
C:\> reg query  HKLM\SYSTEM\ControlSet001\Control\SessionManager\KnownDLLs
```
# LOGS

## Copy event logs:
```
C:\> wevtutil epl Security C:\<BACK UPPATH>\mylogs.evtx
C:\> wevtutil epl System C:\<BACK UPPATH>\mylogs.evtx
C:\> wevtutil epl Application C:\<BACK UPPATH>\mylogs.evtx
```
## Get list of logs remotely:
```
Ref. https://technet.microsoft.com/enus/sysinternals/psloglist.aspx

C:\> psloglist \\<REMOTE COMPUTER> -accepteula -h 12 -x
```

## Clear all logs and start a baseline log to monitor:
```
PS C:\> wevtutil el I Foreach-Object {wevtutil cl"$_"}
```

## List log filenames and path location:
```
C:\> wmic nteventlog get path,filename,writeable
```

## Take pre breach log export:
```
PS C:\> wevtutil el I ForEach-Object{Get-Eventlog -Log "$_" I Export-Csv -Path (:\<BASELINE LOG>,csv -Append}
```
## Take post breach log export:
```
PS C:\> wevtutil el I ForEach-Object{Get-EventLog -Log"$_" I Export-Csv -Path C:\<POST BASELINELOG>,CSV -Append}
```

## Compare two files baseline and post breach logs:
```
PS C:\> Compare-Object -ReferenceObject $(GetContent"C:\<PATH TO FILE>\<ORIGINAL BASELINELOGS>.txt") -DifferenceObject $(Get-Content"C:\<PATH TO FILE>\<POST BASELINE LOGS>.txt") >><DIFFERENCES LOG>.txt
```
## This deletes all logs:
```
PS C:\> wevtutil el I Foreach-Object {wevtutil cl"$_"}
```

## FILES, DRIVES AND SHARES INFORMATION
```
C:\> net use \\<TARGET IP ADDRESS>
C:\> net share
C:\> net session
C:\> wmic volume list brief
C:\> wmic logicaldisk getdescription,filesystem,name,size
C:\> wmic share get name,path
```

## Find multiple file types or a file:
```
C:\> dir /A /5 /T:A *,exe *,dll *,bat *·PS1 *,zip
C:\> dir /A /5 /T:A <BAD FILE NAME>,exe
```

## Find executable (.exe) files newer than Jan 1, 2017:
```
C:\> forfiles /p C:\ /M *,exe /5 /0 +1/1/2017 /C"cmd /c echo @fdate @ftime @path"
```

## Find multiple files types using loop:
```
C:\> for %G in (.exe, .dll, .bat, .ps) do forfiles -p "C:" -m *%G -s -d +1/1/2017 -c "cmd /c echo @fdate@ftime @path"
```

## Search for files newer than date:
```
C:\> forfiles /PC:\ /5 /0 +1/01/2017 /C "cmd /c echo @path @fdate"
```

## Find large files: (example <20 MB)
```
C:\> forfiles /5 /M * /C "cmd /c if @fsize GEO 2097152 echo @path @fsize"
```

## Find files with Alternate Data Streams:

![Ref](https://technet.microsoft.com/enus/sysinternals/streams.aspx)
```
C:\> streams -s <FILE OR DIRECTORY>Find files with bad signature into csv:
```
![Ref](https://technet.microsoft.com/enus/sysinternals/bb897441.aspx)
```
C:\> sigcheck -c -h -s -u -nobanner <FILE OR DIRECTORY> > <OUTPUT FILENAME>,csv
```

## Find and show only unsigned files with bad signature in C:
```
C:\> sigcheck -e -u -vr -s C:\
```

## List loaded unsigned Dlls:
![Ref](https://technet.microsoft.com/enus/sysinternals/bb896656.aspx)
```
C:\> listdlls.exe -u
C:\> listdlls.exe -u <PROCESS NAME OR PID>
```

## Run Malware scan (Windows Defender) offline:
![Ref](http://windows.microsoft.com/enus/windows/what-is-windows-defender-offline)
```
C:\> MpCmdRun.exe -SignatureUpdate
C:\> MpCmdRun.exe -Scan
```
