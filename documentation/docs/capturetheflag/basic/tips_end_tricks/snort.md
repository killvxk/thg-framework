# SNORT RULES
## Snort Rules to detect Meterpreter traffic:
```
Ref.https://blog.didierstevens.com/2015/06/16/metasploit-meterpreter-reverse-https-snort-rule/

alert tcp $HOME_NET any-> $EXTERNAL_NET $HTTP_PORTS
(msg:"Metasploit User Agent String";
flow:to_server,established; content:"User-Agentl3al
Mozilla/4,0 (compatible\; MSIE 6.0\; Windows NT
5.1) l0d 0al"; http_header; classtype:trojanactivity;
reference:url,blog,didierstevens.com/2015/03/16/quic
kpost-metasploit-user-agent-strings/; sid:1618000;
rev:1;)

alert tcp $HOME_NET any-> $EXTERNAL_NET $HTTP_PORTS
( msg: "Metasploit User Agent St ring";
flow:to_server,established; content:"User-Agentl3al
Mozilla/4.0 (compatible\; MSIE 6,1\; Windows NT) l0d
0al"; http_header; classtype:trojan-activity;
reference:url,blog,didierstevens.com/2015/03/16/quic
kpost-metasploit-user-agent-strings/; sid:1618001;
rev: 1;)

alert tcp $HOME_NET any-> $EXTERNAL_NET $HTTP_PORTS
(msg: "Metasploit User Agent String";
flow:to_server,established; content:"User-Agentl3al
Mozilla/4,0 (compatible\; MSIE 7,0\; Windows NT
6.0) l0d 0al"; http_header; classtype:trojanactivity;
reference:url,blog.didierstevens.com/2015/03/16/quic
kpost-metasploit-user-agent-strings/; sid:1618002;
rev: 1;)

alert tcp $HOME_NET any-> $EXTERNAL_NET $HTTP_PORTS
(msg:"Metasploit User Agent String";
flow:to_server,established; content:"User-Agentl3al
Mozilla/4,0 (compatible\; MSIE 7,0\; Windows NT
6,0\; Trident/4,0\; SIMBAR={7DB0F6DE-8DE7-4841-9084-
28FA914B0F2E}\; SLCCl\; ,Nl0d 0al"; http_header;
classtype:trojan-activity;
reference:url,blog.didierstevens.com/2015/03/16/quic
kpost-metasploit-user-agent-strings/; sid:1618003;
rev: 1;)

alert tcp $HOME_NET any -> $EXTERNAL_NET $HTTP_PORTS
(msg:"Metasploit User Agent String";
flow:to_server,established; content:"User-Agentl3al
Mozilla/4.0 (compatible\; Metasploit RSPEC)l0d 0al";
http_header; classtype:trojan-activity;
reference:url,blog,didierstevens.com/2015/03/16/quic
kpost-metasploit-user-agent-strings/; sid:1618004;
rev: 1;)

alert tcp $HOME_NET any -> $EXTERNAL_NET $HTTP_PORTS
(msg:"Metasploit User Agent String";
flow:to_server,established; content:"User-Agentl3al
Mozilla/5,0 (Windows\; U\; Windows NT 5,1\; en-US)
AppleWebKit/525,13 (KHTML, like Gecko)
Chrome/4.0.221.6 Safari/525,13l0d 0al"; http_header;
classtype:trojan-activity;
reference:url,blog.didierstevens.com/2015/03/16/quic
kpost-metasploit-user-agent-strings/; sid:1618005;
rev: 1;)

alert tcp $HOME_NET any -> $EXTERNAL_NET $HTTP_PORTS
( msg: "Metasploit User Agent St ring";
flow:to_server,established; content:"User-Agentl3al
Mozilla/5.0 (compatible\; Googlebot/2.1\;
+http://www.google.com/bot.html) l0d 0al";
http_header; classtype:trojan-activity;
reference:url,blog,didierstevens.com/2015/03/16/quic
kpost-metasploit-user-agent-strings/; sid:1618006;
rev: 1;)

alert tcp $HOME_NET any -> $EXTERNAL_NET $HTTP_PORTS
(msg: "Metasploit User Agent St ring";
flow:to_server,established; content:"User-Agentl3al
Mozilla/5,0 (compatible\; MSIE 10,0\; Windows NT
6,1\; Trident/6,0) l0d 0al"; http_header;
classtype:trojan-activity;
reference:url,blog.didierstevens.com/2015/03/16/quic
kpost-metasploit-user-agent-strings/; sid:1618007;
rev: 1;)
```
## Snort Rules to detect PSEXEC traffic:
```
Ref. https://github.com/John-Lin/dockersnort/blob/master/snortrules-snapshot2972/rules/policy-other.rules

alert tcp $HOME_NET any -> $HOME_NET [139,445]
(msg:"POLICY-OTHER use of psexec remote
admin ist rat ion tool"; flow: to_server, established;
content:" IFFISMB1A2I"; depth:5; offset:4;
content:"ISC
.00 I p I 00 Is I 00 I e I 00 Ix I 00 I e I 00 I c I 00 I s I 00 Iv I 00 I c" ;
nocase; metadata:service netbios-ssn;
reference:url,technet.microsoft.com/enus/sysinternals/bb897553.aspx;
classtype:policyviolation;
sid:24008; rev:1;)

alert tcp $HOME_NET any -> $HOME_NET [139,445]
(msg:"POLICY-OTHER use of psexec remote
administration tool SMBv2";
flow:to_server,established; content:"IFEISMB";
depth:8; nocase; content:"105 001"; within:2;
distance:8;
content:"Pl001Sl00IEl00IXl00IEl00ISl00IVl00ICl00I";
fast_pattern:only; metadata:service netbios-ssn;
reference:url,technet.microsoft,com/enus/sysinternals/bb897553.aspx[l];
classtype:policyviolation;
sid:30281; rev:1;)

```
