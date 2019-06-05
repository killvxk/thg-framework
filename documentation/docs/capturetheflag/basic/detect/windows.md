## Increase Log size to support increased auditing:
```
C:\> reg add HKLM\Software\Policies\Microsoft\Windows\Eventlog\Application /v MaxSize /t REG_DWORD /d 0x19000
C:\> reg add HKLM\Software\Policies\Microsoft\Windows\Eventlog\Security /v MaxSize /t REG_DWORD /d 0x64000
C:\> reg add HKLM\Software\Policies\Microsoft\Windows\EventLog\System /v MaxSize /t REG_DWORD /d 0x19000
```
## Check settings of Security log:
```
C:\> wevtutil gl Security
```
## Check settings of audit policies:
```
C:\> auditpol /get /category:*
```

## Set Log Auditing on for Success and/or Failure on All Categories:
```
C:\> auditpol /set /category:* /success:enable /failure:enable
```

## Set Log Auditing on for Success and/or Failure on Subcategories:
```
C:\> auditpol /set /subcategory: "Detailed FileShare" /success:enable /failure:enable
C:\> auditpol /set /subcategory:"File System"/success:enable /failure:enable
C:\> auditpol /set /subcategory:"Security System Extension" /success:enable /failure:enable
C:\> auditpol /set /subcategory:"System Integrity"/success:enable /failure:enable
C:\> auditpol /set /subcategory:"Security StateChange" /success:enable /failure:enable
C:\> auditpol /set /subcategory:"Other SystemEvents" /success:enable /failure:enable
C:\> auditpol /set /subcategory:"System Integrity"/success:enable /failure:enable
C:\> auditpol /set /subcategory:"Logon" /success:enable /failure:enable
C:\> auditpol /set /subcategory:"Logoff" /success:enable /failure:enable
C:\> auditpol /set /subcategory:"Account Lockout" /success:enable /failure:enable
C:\> auditpol /set /subcategory:"Other Logon/Logoff Events" /success:enable /failure:enable
C:\> auditpol /set /subcategory:"Network Policy Server" /success:enable /failure:enable
C:\> auditpol /set /subcategory:"Registry" /success:enable /failure:enable
C:\> auditpol /set /subcategory:"SAM" /success:enable /failure:enable
C:\> auditpol /set /subcategory:"Certification Services" /success:enable /failure:enable
C:\> auditpol /set /subcategory:"Application Generated" /success:enable /failure:enable
C:\> auditpol /set /subcategory: "Handle Manipulation" /success:enable /failure:enable
C:\> auditpol /set /subcategory:"file Share" /success:enable /failure:enable
C:\> auditpol /set /subcategory:"filtering Platform Packet Drop" /success:enable /failure:enable
C:\> auditpol /set /subcategory:"Filtering Platform Connection" /success:enable /failure:enable
C:\> auditpol /set /subcategory:"Other Object Access Events" /success:enable /failure:enable
C:\> auditpol /set /subcategory: "Detailed File Share" /success:enable /failure:enable
C:\> auditpol /set /subcategory: "Sensitive Privilege Use" /success:enable /failure:enable
C:\> auditpol /set /subcategory: "Non Sensitive Privilege Use" /success:enable /failure:enable
C:\> auditpol /set /subcategory: "Other Privilege Use Events" /success:enable /failure:enable
C:\> auditpol /set /subcategory:"Process Termination" /success:enable /failure:enable
C:\> auditpol /set /subcategory: "DPAPI Activity" /success:enable /failure:enable
C:\> auditpol /set /subcategory: "RPC Events" /success:enable /failure:enable
C:\> auditpol /set /subcategory:"Process Creation" /success:enable /failure:enable
C:\> auditpol /set /subcategory:"Audit Policy Change" /success:enable /failure:enable
C:\> auditpol /set /subcategory: "Authentication Policy Change" /success:enable /failure:enable
C:\> auditpol /set /subcategory: "Authorization Policy Change" /success:enable /failure:enable
C:\> auditpol /set /subcategory: "MPSSVC Rule-Level Policy Change" /success:enable /failure:enable
C:\> auditpol /set /subcategory:"Filtering Platform Policy Change" /success:enable /failure:enable
C:\> auditpol /set /subcategory:"Other Policy Change Events" /success:enable /failure:enable
C:\> auditpol /set /subcategory:"User Account Management" /success:enable /failure:enable
C:\> auditpol /set /subcategory:"Computer Account Management" /success:enable /failure:enable
C:\> auditpol /set /subcategory:"Security Group Management" /success:enable /failure:enable
C:\> auditpol /set /subcategory:"Distribution Group Management" /success:enable /failure:enable
C:\> auditpol /set /subcategory:"Application Group Management" /success:enable /failure:enable
C:\> auditpol /set /subcategory:"Other Account Management Events" /success:enable /failure:enable
C:\> auditpol /set /subcategory:"Directory Service Changes" /success:enable /failure:enable
C:\> auditpol / set /subcategory: "Directory Service Replication" /success:enable /failure:enable
C:\> auditpol /set /subcategory:"Detailed Directory Service Replication" /success:enable /failure:enable
C:\> auditpol /set /subcategory:"Directory Service Access" /success:enable /failure:enable
C:\> auditpol /set /subcategory:"Kerberos Service Ticket Operations" /success:enable /failure:enable
C:\> auditpol /set /subcategory:"Other Account Logan Events" /success:enable /failure:enable
C:\> audit pol /set /subcategory: "Kerberos Authentication Service" /success:enable /failure:enable
C:\> auditpol /set /subcategory:"Credential Validation" /success:enable /failure:enable
```
## Check for list of available logs, size, retention limit:
```
PS C:\> Get-Eventlog -list
```
## Partial list of Key Security Log Auditing events to monitor:
```
PS C:\> Get-Eventlog -newest 5 -logname applicationI Format-List
```

## Show log from remote system:
```
PS C:\> Show-Eventlog -computername <SERVER NAME>Get a specific list of events based on Event ID:
PS C:\> Get-Eventlog Security I ? { $_.Eventid -eq4800}
PS C:\> Get-WinEvent -FilterHashtable@{LogName="Secu rity"; ID=4774}
```

## Account Logon - Audit Credential Validation Last 14 Days:
```
PS C:\> Get-Eventlog Security 4768,4771,4772,4769,4770,4649,4778,4779,4800,4801,48 02,4803,5378,5632,5633 -after ((get-date).addDays(-14))
```

## Account - Logon/Logoff:
```
PS C:\> Get-Eventlog Security 4625,4634,4647,4624,4625,4648,4675,6272,6273,6274,62 75,6276,6277,6278,6279,6280,4649,4778,4779,4800,4801,4802,4803,5378,5632,5633,4964 -after ((getdate).addDays(-1))
```

## Account Management - Audit Application Group Management:
```
PS C:\> Get-Eventlog Security 4783,4784,4785,4786,4787,4788,4789,4790,4741,4742,47 43,4744,4745,4746,4747,4748,4749,4750,4751,4752,4753,4759,4760,4761,4762,4782,4793,4727,4728,4729,4730,4731,4732,4733,4734,4735,4737,4754,4755,4756,4757,4758,4764,4720,4722,4723,4724,4725,4726,4738,4740,4765,4766,4767,4780,4781,4794,5376,5377 -after ((getdate).addDays(-1))
```

## Detailed Tracking - Audit DPAPI Activity, Process Termination, RPC Events:
```
PS C:\> Get-EventLog Security 4692,4693,4694,4695,4689,5712 -after ((getdate).addDays(-1))
```

## Domain Service Access - Audit Directory Service Access:
```
PS C:\> Get-EventLog Security 4662,5136,5137,5138,5139,5141 -after ((getdate).addDays(-1))
```

## Object Access - Audit File Share, File System, SAM,Registry, Certifications:
```
PS C:\> Get-EventLog Security 4671,4691,4698,4699,4700,4701,4702,5148,5149,5888,5889,5890,4657,5039,4659,4660,4661,4663,4656,4658,4690,4874,4875,4880,4881,4882,4884,4885,4888,4890,4891,4892,4895,4896,4898,5145,5140,5142,5143,5144,5168,5140,5142,5143,5144,5168,5140,5142,5143,5144,5168,4664,4985,5152,5153,5031,5140,5150,5151,5154,5155,5156,5157,5158,5159 -after ((get-date).addDays(-1))
```

## Policy Change - Audit Policy Change, Microsoft Protection Service, Windows Filtering Platform:
```
PS C:\> Get-EventLog Security 4715,4719,4817,4902,4904,4905,4906,4907,4908,4912,4713,4716,4717,4718,4739,4864,4865,4866,4867,4704,4705,4706,4707,4714,4944,4945,4946,4947,4948,4949,4950,4951,4952,4953,4954,4956,4957,4958,5046,5047,5048,5449,5450,4670 -after ((get-date).addDays(-1))
```

## Privilege Use - Audit Non-Sensitive/Sensitive Privilege Use:
```
PS C:\> Get-EventLog Security 4672,4673,4674 -after((get-date),addDays(-1))
```

## System - Audit Security State Change, Security System Extension, System Integrity, System Events:
```
PS C:\> Get-Eventlog Security 5024,5025,5027,5028,5029,5030,5032,5033,5034,5035,5037,5058,5059,6400,6401,6402,6403,6404,6405,6406,6407,4608,4609 ,4616, 4621, 4610, 4611, 4614,4622,4697,4612,4615,4618,4816,5038,5056,5057,5060,5061,5062,6281 -after ((get-date).addDays(-1))
```

## Add Microsoft IIS cmdlet:
```
PS C:\> add-pssnapin WebAdministration
PS C:\> Import-Module WebAdministration Get IIS Website info:
PS C:\> Get-IISSite Get IIS Log Path Location:
PS C:\> (Get-WebConfigurationProperty '/system.applicationHost/sites/siteDefaults' -Name 'logfile.directory').Value
```
## Set variable for IIS Log Path (default path):
```
PS C:\> $LogDirPath = "C:\inetpub\logs\LogFiles\W3SVCl"
```
## Get IIS HTTP log file list from Last 7 days:
```
PS C:\> Get-Child!tem -Path C:\inetpub\logs\LogFiles\w3svcl -recurse I WhereObject {$_. lastwritetime -lt (get-date).addDays(-7)}
```
## View IIS Logs (Using $LogDirPath variable set above):
```
PS C:\> Get-Content $LogDirPath\*, log I%{$_ -replace '#Fields: ', "} I?{$_ -notmatch ""#'} I ConvertFrom-Csv -Delimiter '
```

## View IIS Logs:
```
PS C:\> Get-Content <!IS LOG FILE NAME>, log I%{$_ -replace '#Fields: ', ''} 17{$_ -notmatch 'A#'} I ConvertFrom-Csv -Delimiter ' 'Find in IIS logs IP address 192.168.*·* pattern:
PS C:\> Select-String -Path $LogDirPath\*, log -Pattern '192,168,*,*'
```

## Find in IIS logs common SQL injection patterns:
```
PS C:\> Select-String -Path $LogDirPath\*, log'(@@version) I (sqlmap) I (Connect\(\)) I (cast\() I (char\() I ( bcha r\ () I ( sysdatabases) I ( \ (select) I (convert\ () I ( Connect\ () I ( count\() I (sys objects)'
```

