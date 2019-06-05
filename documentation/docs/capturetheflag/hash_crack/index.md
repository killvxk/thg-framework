# INTRO
This manual is meant to be a reference guide for cracking tool usage and
supportive tools that assist network defenders and pentesters in password
recovery (cracking). This manual will not be covering the installation of these
tools, but will include references to their proper installation, and if all else fails,
Google. Updates and additions to this manual are planned yearly as
advancements in cracking evolve. Password recovery is a battle against math,
time, cost, and human behavior; and much like any battle, the tactics are
constantly evolving.

# ACKNOWLEDGEMENTS

This community would not enjoy the success and diversity without the following
community members and contributors: Alexander ‘Solar Designer’ Peslvak,
John The Ripper Team, & Community Jens ‘atom’ Steube, Hashcat Team, &
Devoted Hashcat Forum Community Jeremi ‘epixoip’ Gosney
Korelogic & the Crack Me If You Can Contest Robin ‘DigiNinja’ Wood (Pipal &
CeWL) CynoSure Prime Team
Chris ‘Unix-ninja’ Aurelio
Per Thorsheim (PasswordsCon)
Blandyuk & Rurapenthe (HashKiller Contest) Peter ‘iphelix’ Kacherginsky
(PACK) Royce ‘tychotithonus’ Williams ‘Waffle’

And many, many, many more contributors. If a name was excluded from the
above list please reach out and the next version will give them their due credit.
Lastly, the tools, research, and file_suport covered in the book are the result of
people’s hard work. As such, I HIGHLY encourage all readers to DONATE to
help assist in their efforts. A portion of the proceeds from this book will be
distributed to the various researchers/projects.

# REQUIRED SOFTWARE
In order to follow many of the techniques in this manual, you will want to install
the following software on your Windows or *NIX host. This book does not
cover how to install said software and assumes you were able to follow the
included links and extensive support websites.
## HASHCAT v3.6 (or newer)
https://hashcat.net/hashcat/
## JOHN THE RIPPER (v1.8.0 JUMBO)
http://www.openwall.com/john/
## PACK V0.0.4 (Password Analysis and Cracking Toolkit)
http://thesprawl.org/projects/pack/
## Hashcat-utils v1.7
https://hashcat.net/wiki/doku.php?id=hashcat_utils
## Additionally you will need dictionaries/wordlists and highly recommend the below sources: WEAKPASS DICTIONARY
https://weakpass.com/wordlist
## CRACKSTATION DICTIONARY
https://crackstation.net/buy-crackstation-wordlist-password-cracking-dictionary.htm
## SKULL SECURITY WORDLISTS
https://wiki.skullsecurity.org/index.php?title=Passwords
Throughout the manual, generic names have been given to the various inputs
required in a cracking commands structure. Legend description is below:

# COMMAND STRUCTURE LEGEND
## hashcat
Generic representation of the various Hashcat binary names

## john
Generic representation of the John the Ripper binary names

## #type
Hash type; which is an abbreviation in John or a number in Hashcat

## hash.txt
File containing target hashes to be cracked

## dict.txt
File containing dictionary/wordlist

## rule.txt
File containing permutation rules to alter dict.txt input

## passwords.txt
File containing cracked password results

## outfile.txt
File containing results of

some functions output Lastly, as a good reference for testing various hash types
to place into your “hash.txt” file, the below sites contain all the various hashing
algorithms and example output tailored for each cracking tool: HASHCAT
HASH FORMAT EXAMPLES
https://hashcat.net/wiki/doku.php?id=example_hashes
JOHN THE RIPPER HASH FORMAT EXAMPLES
http://pentestmonkey.net/cheat-sheet/john-the-ripper-hash-formats
http://openwall.info/wiki/john/sample-hashes