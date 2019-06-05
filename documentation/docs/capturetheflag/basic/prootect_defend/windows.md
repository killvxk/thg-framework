# DISABLE/STOP SERVICES
## Get a list of services and disable or stop:
```
C:\> sc query
C:\> sc config "<SERVICE NAME>" start= disabled
C:\> sc stop "<SERVICE NAME>"
C:\> wmic service where name='<SERVICE NAME>' callChangeStartmode Disabled
```
# HOST SYSTEM FIREWALLS
## Show all rules:
```
C:\> netsh advfirewall firewall show rule name=all
```
## Set firewall on/off:
```
C:\> netsh advfirewall set currentprofile state on
C:\> netsh advfirewall set currentprofilefirewallpolicy blockinboundalways,allowoutbound
C:\> netsh advfirewall set publicprofile state on
C:\> netsh advfirewall set privateprofile state on
C:\> netsh advfirewall set domainprofile state on
C:\> netsh advfirewall set allprofile state on
C:\> netsh advfirewall set allprof ile state
```
## offSet firewall rules examples:
```
C:\> netsh advfirewall firewall add rule name="OpenPort 80" dir=in action=allow protocol=TCPlocalport=80
C:\> netsh advfirewall firewall add rule name="MyApplication" dir=in action=al lowprogram="C:\MyApp\MyApp.exe" enable=yes
C:\> netsh advfirewall firewall add rule name="MyApplication" dir=in action=al lowprogram="C:\MyApp\MyApp.exe" enable=yesremoteip=157.60.0.1,172.16.0.0/16,Local5ubnetprof i le=domain
C:\> netsh advfirewall firewall add rule name="MyApplication" dir=in action=allowprogram="C:\MyApp\MyApp.exe" enable=yesremoteip=157.60.0.1,172.16.0.0/16,LocalSubnetprofile=domain
C:\> netsh advfirewall firewall add rule name="MyApplication" dir=in action=al lowprogram="C:\MyApp\MyApp.exe" enable=yesremoteip=157.60.0.1,172.16.0.0/16,Local5ubnetprofile=private
C:\> netsh advfirewall firewall delete rulename=rule name program="C:\MyApp\MyApp.exe"
C:\> netsh advfirewall firewall delete rulename=rule name protocol=udp localport=500
C:\> netsh advfirewall firewall set rulegroup=" remote desktop" new enable=Yes prof ile=domain
C:\> netsh advfirewall firewall set rulegroup="remote desktop" new enable=No profile=publicSetup
```
## togging location:
```
C:\> netsh advfirewall set currentprofile logging
C:\<LOCATION>\<FILE NAME>Windows firewall tog location and settings:
C:\> more %systemroot%\system32\LogFiles\Firewall\pfirewall.log
C:\> netsh advfirewall set allprofile loggingmaxfilesize 4096
C:\> netsh advfirewall set allprofile loggingdroppedconnections enable
C:\> netsh advfirewall set allprofile loggingallowedconnections enable
```

## Display firewall logs:
```
PS C:\> Get-Content$env:systemroot\system32\LogFiles\Firewall\pfirewall. log
```

# PASSWORDS

## Change password:
```
C:\> net user <USER NAME> * /domain
C:\> net user <USER NAME> <NEW PASSWORD>
```

## Change password remotely:

![Ref](https://technet.microsoft.com/enus/sysinternals/bb897543)
```
C:\> pspasswd.exe \\<IP ADDRESS or NAME OF REMOTECOMPUTER> -u <REMOTE USER NAME> -p <NEW PASSWORD>
```

## Change password remotely:
```
PS C:\> pspasswd.exe \\<IP ADDRESS or NAME OF REMOTECOMPUTER>HOST FILE
```

## Flush DNS of malicious domain/IP:
```
C:\> ipconfig /flushdns
```
## Flush NetBios cache of host/IP:
```
C:\> nbtstat -R
```

## Add new malicious domain to hosts file, and route tolocalhost:
```
C:\> echo 127.0.0.1 <MALICIOUS DOMAIN> >>
C:\Windows\System32\drivers\etc\hosts
```
## Check if hosts file is working, by sending ping to 127.0.0.1:
```
C:\> ping <MALICIOUS DOMAIN> -n 1
```
## WHITELIST Use a Proxy Auto Config(PAC) file to create Bad URL or IP List (IE, Firefox, Chrome):

```
function FindProxyForURL(url, host) {
// II Send bad DNS name to the proxy
    if (dnsDomainis(host, ".badsite.com"))
        return "PROXY http:11127.0.0.1:8080";
// II Send bad IPs to the proxy
    if (isinNet(myipAddress(), "222.222.222.222","255.255.255.0"))
        return "PROXY http:11127.0.0.1:8080";
//II All other traffic bypass proxy
        return "DIRECT";
}
```

# APPLICATION RESTRICTIONS

## Applocker - Server 2008 R2 or Windows 7 or higher:
## Using GUI Wizard configure:
* Executable Rules (. exe, . com)
* DLL Rules ( .dll, .ocx)
* Script Rules (.psl, .bat, .cmd, .vbs, .js)
* Windows Install Rules ( .msi, .msp, .mst)

# Steps to employ Applocker (GUI is needed for digitalsigned app restrictions):

## Step 1:
```
Create a new GPO.
```
## Step 2:
```
Right-click on it to edit, and then navigate
through Computer Configuration, Policies, Windows
Settings, Security Settings, Application Control
Policies and Applocker.
Click Configure Rule Enforcement.
```
## Step 3:
```
Under Executable Rules, check the Configured
box and then make sure Enforce Rules is selected
from the drop-down box. Click OK.
```
## Step 4:
```
In the left pane, click Executable Rules.
Step 5: Right-click in the right pane and select
Create New Rule.
```
## Step 6:
```
On the Before You Begin screen, click Next.
```
## Step 7:
```
On the Permissions screen, click Next.
```
## Step 8:
```
On the Conditions screen, select the
Publisher condition and click Next.
```
## Step 9:
```
Click the Browse button and browse to any
executable file on your system. It doesn't matter
which.
```
## Step 10:
```
Drag the slider up to Any Publisher and
then click Next.
```
## Step 11:
```
Click Next on the Exceptions screen.
```
## Step 12:
```
Name policy, Example uonly run executables
that are signed" and click Create.
```
## Step 13:
```
If this is your first time creating an
Applocker policy, Windows will prompt you to create
default rule, click Yes.
```
## Step 14:
```
Ensure Application Identity Service isRunning.

C:\> net start AppIDSvc
C:\> REG add"HKLM\SYSTEM\CurrentControlSet\services\AppIDSvc" /v Start /t REG_DWORD /d 2 /f
```
## Step 15:
```
Changes require reboot.
C:\ shutdown.exe /r
C:\ shutdown.exe /r /m \\<IP ADDRESS OR COMPUTERNAME> /f
```

## Add the Applocker cmdlets into PowerShell:
```
PS C:\> import-module Applocker
```
## Gets the file information for all of the executable files and scripts in the directory
```
C:\Windows\System32:
PS C:\> Get-ApplockerFileinformation -Directory
C:\Windows\System32\ -Recurse -FileType Exe, Script
```
## Create a Applocker Policy that allow rules for all of the executable files in C:\Windows\System32:
```
PS C:\> Get-Childitem C:\Windows\System32\*,exe IGet-ApplockerFileinformation I New-ApplockerPolicy -RuleType Publisher, Hash -User Everyone -RuleNamePrefix System32
```
## Sets the local Applocker policy to the policy specified in C:\Policy.xml:
```
PS C:\> Set-AppLockerPolicy -XMLPolicy C:\Policy.xml
```
## Uses the Applocker policy in C:\Policy.xml to test whether calc.exe and notepad.exe are allowed to run for users who are members of the Everyone group. If you do not specify a group, the Everyone group is used by default:
```
PS C:\> Test-AppLockerPolicy -XMLPolicy
C:\Policy.xml -Path C:\Windows\System32\calc.exe,
C:\Windows\System32\notepad.exe -User Everyone
```
## Review how many times a file would have been blocked from running if rules were enforced:
```
PS C:\> Get-ApplockerFileinformation -Eventlog -Logname "Microsoft-Windows-Applocker\EXE and DLL" -EventType Audited -Statistics
```

## Creates a new Applocker policy from the auditedevents in the local Microsoft-Windows-Applocker/EXE and DLL event log, applied to <GROUP> and current Applocker policy will be overwritten:
```
PS C:\> Get-ApplockerFileinformation -Eventlog -LogPath "Microsoft-Windows-AppLocker/EXE and DLL" -EventType Audited I New-ApplockerPolicy -RuleType Publisher,Hash -User domain\<GROUP> -IgnoreMissingFileinformation I Set-ApplockerPolicy -LDAP "LDAP://<DC>,<DOMAIN>.com/CN={31B2F340-016D11D2-945F00C04FB984F9},CN=Policies,CN=System,DC=<DOMAIN>,DC=com"
```

## Export the local Applocker policy, comparing User'sexplicitly denied access to run, and output textfile:
```
PS C:\> Get-AppLockerPolicy -Local I TestAppLockerPolicy -Path C:\Windows\System32\*,exe -User domain\<USER NAME> -Filter Denied I Format-List -Property Path > C:\DeniedFiles.txt
```

## Export the results of the test to a file foranalysis:

```
PS C:\> Get-Childitem <DirectoryPathtoReview> -Filter <FileExtensionFilter> -Recurse I Convert-Path I Test-ApplockerPolicy -XMLPolicy <PathToExportedPolicyFile> -User <domain\username> -Filter <TypeofRuletoFilterFor> I Export-CSV <PathToExportResultsTo.CSV>
```

## GridView list of any local rules applicable:
```
PS C:\> Get-AppLockerPolicy -Local -Xml I OutGridView
```


# IPSEC

## Create a IPSEC Local Security Policy, applied to any connection, any protocol, and using a preshared key:
```
C:\> netsh ipsec static add filter filterlist=MyIPsecFilter srcaddr=Any dstaddr=Any protocol=ANY
C:\> netsh ipsec static add filteraction name=MyIPsecAction action=negotiate
C:\> netsh ipsec static add policy name=MyIPsecPolicy assign=yes
C:\> netsh ipsec static add rule name=MyIPsecRule policy=MyIPsecPolicy filterlist=MyIPsecFilter filteraction=MyIPsecAction conntype=all activate=yes psk=<PASSWORD>
```

## Add rule to allow web browsing port 80(HTTP) and 443(HTTPS) over IPSEC:
```
C:\> netsh ipsec static add filteraction name=Allow action=permit
C:\> netsh ipsec static add filter filterlist=WebFilter srcaddr=Any dstaddr=Any protocol=TCP dstport=80
C:\> netsh ipsec static add filter filterlist=WebFilter srcaddr=Any dstaddr=Any protocol=TCP dstport=443
C:\> netsh ipsec static add rule name=WebAllow policy=MyIPsecPolicy filterlist=WebFilter filteraction=Allow conntype=all activate=yes psk=<PASSWORD>
```


## Shows the IPSEC Local Security Policy with name "MyIPsecPolicy":
```
C:\> netsh ipsec static show policy name=MyIPsecPolicy
```
## Stop or Unassign a IPSEC Policy:
```
C:\> netsh ipsec static set policy name=MyIPsecPolicy
```
## Create a IPSEC Advance Firewall Rule and Policy and preshared key from and to any connections:
```
C:\> netsh advfirewall consec add rule name="IPSEC" endpointl=any endpoint2=any action=requireinrequireout qmsecmethods=default
```

## Require IPSEC preshared key on all outgoing requests:
```
C:\> netsh advfirewall firewall add rule name=uIPSEC_Out" dir=out action=allow enable=yes profile=any localip=any remoteip=any protocol=any interfacetype=any security=authenticate
```
## Create a rule for web browsing:
```
C:\> netsh advfirewall firewall add rule name="Allow Outbound Port 8011 dir=out localport=80 protocol=TCP action=allow
```
## Create a rule for DNS:
```
C:\> netsh advfirewall firewall add rule name="Allow Outbound Port 5311 dir=out localport=53 protocol=UDP action=allow
```
## Delete ISPEC Rule:
```
C:\> netsh advfirewall firewall delete rule name="IPSEC_RULE"
```

# ACTIVE DIRECTORY (AD) - GROUP POLICY OBJECT (GPO)

## Get and force new policies:
```
C:\> gpupdate /force
C:\> gpupdate /sync
```

## Audit Success and Failure for user Bob:
```
C:\> auditpol /set /user:bob /category:"DetailedTracking" /include /success:enable /failure:enable
```

## Create an Organization Unit to move suspected or infected users and machines:
```
C:\> dsadd OU <QUARANTINE BAD OU>
```


## Move an active directory user object into NEW GROUP:
```
PS C:\> Move-ADObject 'CN=<USER NAME>,CN=<OLD USERGROUP>,DC=<OLD DOMAIN>,DC=<OLD EXTENSION>' -TargetPath 'OU=<NEW USER GROUP>,DC=<OLDDOMAIN>,DC=<OLD EXTENSION>'
```

## Alt Option:
```
C:\> dsmove "CN=<USER NAME>,OU=<OLD USER OU>,DC=<OLDDOMAIN>,DC=<OLD EXTENSION>" -newparent OU=<NEW USERGROUP>,DC=<OLD DOMAIN>,DC=<OLD EXTENSION>
```


# STAND ALONE SYSTEM - WITHOUT ACTIVE DIRECTORY (AD)

## Disallow running a .exe file:
```
C:\> reg add "HKCU\Software\Microsoft\Windows\CurrentVersion\Policies\Explorer" /v DisallowRun /t REG_DWORD /d"00000001" /f
C:\> reg add "HKCU\Software\Microsoft\Windows\CurrentVersion\Policies\Explorer\DisallowRun" /v badfile.exe /t REG_SZ/d <BAD FILE NAME>.exe /f
```

## Disable Remote Desktop:
```
C:\> reg add "HKLM\SYSTEM\Cu rrentCont ro lSet\Cont ro l \ TerminalServer" /f /v fDenyTSConnections /t REG_DWORD /d 1
```

## Send NTLMv2 response only/refuse LM and NTLM:(Windows 7 default)
```
C:\> reg add HKLM\SYSTEM\CurrentControlSet\Control\Lsa\ /vlmcompatibilitylevel /t REG_DWORD /d 5 /f
```
## Restrict Anonymous Access:
```
C:\> reg add HKLM\SYSTEM\CurrentControlSet\Control\Lsa /v restrictanonymous /t REG_DWORD /d 1 /f
```

## Do not allow anonymous enumeration of SAM accounts and shares:
```
C:\> reg add HKLM\SYSTEM\CurrentControlSet\Control\Lsa /v restrictanonymoussam /t REG_DWORD /d 1 /f
```

## Disable IPV6:
```
C:\> reg add HKLM\SYSTEM\CurrentControlSet\services\TCPIP6\Parameters /v DisabledComponents /t REG_DWORD /d 255 /f
```
## Disable sticky keys:
```
C:\> reg add "HKCU\ControlPanel\Accessibility\StickyKeys" /v Flags /t REG_SZ/d 506 /f
```
## Disable Toggle Keys:
```
C:\> reg add "HKCU\ControlPanel \Accessibility\ ToggleKeys" /v Flags /t REG_SZId 58 /f
```
## Disable Filter Keys:
```
C:\> reg add "HKCU\ControlPanel\Accessibility\Keyboard Response" /v Flags /t REG_SZ /d 122 /f
```
## Disable On-screen Keyboard:
```
C:\> reg add HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Authentication\LogonUI /f /v ShowTabletKeyboard /tREG_DWORD /d 0
```

## Disable Administrative Shares - Workstations:
```
C:\> reg add HKLM\SYSTEM\CurrentControlSet\Services\LanmanServer\Parameters /f /v AutoShareWks /t REG_DWORD /d 0
```

## Disable Administrative Shares - Severs
```
C:\> reg add HKLM\SYSTEM\CurrentControlSet\Services\LanmanServer\ Parameters /f /v AutoShareServer /t REG_DWORD /d 0
```

## Remove Creation of Hashes Used to Pass the Hash Attack (Requires password reset and reboot to purgeold hashes):
```
C:\> reg add HKLM\SYSTEM\CurrentControlSet\Control\Lsa /f /v NoLMHash /t REG_DWORD /d 1
```
## To Disable Registry Editor: (High Risk)
```
C:\> reg add HKCU\Software\Microsoft\Windows\CurrentVersion\Policies\System /v DisableRegistryTools /t REG_DWORD /d 1 /f
```
## Disable IE Password Cache:
```
C:\> reg add HKCU\Software\Microsoft\Windows\CurrentVersion\Internet Settings /v DisablePasswordCaching /t REG_DWORD /d 1 /f
```

## Disable CMD prompt:
```
C:\> reg add HKCU\Software\Policies\Microsoft\Windows\System /v DisableCMD /t REG_DWORD /d 1 /f
```


## Disable Admin credentials cache on host when usingRDP:
```
C:\> reg add HKLM\System\CurrentControlSet\Control\Lsa /v DisableRestrictedAdmin /t REG_DWORD /d 0 /f
```
## Do not process the run once list:
```
C:\> reg add HKLM\Software\Microsoft\Windows\CurrentVersion\Policies\Explorer /v DisableLocalMachineRunOnce /t REG_DWORD /d 1
C:\> reg add HKCU\Software\Microsoft\Windows\CurrentVersion\Policies\Explorer /v DisableLocalMachineRunOnce /t REG_DWORD /d 1
```
## Require User Access Control (UAC) Permission:
```
C:\> reg add HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System /v EnableLUA /t REG_DWORD /d 1 /f
```
## Change password at next logon:
```
PS C:\> Set-ADAccountPassword <USER> -NewPassword $newpwd -Reset -PassThru I Set-ADuser -ChangePasswordAtLogon $True
```
## Change password at next logon for OU Group:
```
PS C:\> Get-ADuser -filter "department -eq '<OUGROUP>' -AND enabled -eq 'True 111 I Set-AD user -ChangePasswordAtLogon $True
```

## Enabled Firewall logging:
```
C:\> netsh firewall set logging droppedpacketsconnections = enable
```