# OPENVAS
```
Step 1: Install the server, client and plugin
packages:

# apt-get install openvas-server openvas-client openvas-plugins-base openvas-plugins-dfsg

Step 2: Update the vulnerability database
# openvas-nvt-sync

Step 3: Add a user to run the client:
# openvas-adduser
Step 4: Login: sysadm
Step 5: Authentication (pass/cert) [pass]: [HITENTER]

Step 6: Login password: <PASSWORD>
You will then be asked to add "User rules".

Step 7: Allow this user to scan authorized network
by typing:
accept <YOUR IP ADDRESS OR RANGE>
default deny

Step 8: type ctrl-D to exit, and then accept.

Step 9: Start the server:
# service openvas-server start

Step 10: Set targets to scan:
Create a text file with a list of hosts/networks to
scan.
# vi scanme.txt

Step 11: Add one host, network per line:
<IP ADDRESS OR RANGE>

Step 12: Run scan:
# openvas-client -q 127.0.0.1 9390 sysadm nsrc+ws
scanme.txt openvas-output-.html -T txt -V -x

Step 13: (Optional)run scan with HTML format:
# openvas-client -q 127.0.0.1 9390 sysadm nsrc+ws
scanme.txt openvas-output.txt -T html -V -x

```