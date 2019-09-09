Esta página lista as chaves em uso por [THG committers] [thg-committers] e
pode ser usado para verificar as confirmações de mesclagem feitas em https://gitlab.com/darkcode357/thg-framework/.

### Identidades do Keybase.io

O Keybase.io é usado pelo THG como uma maneira fácil de verificar as identidades dos confirmadores.

Se você é um colaborador do THG HACKER GROUP e precisa de um convite, basta perguntar.

| Gitlab Username                                   | Keybase.io Username                                |
| ------------------------------------------------- | -------------------------------------------------- |
| [@darkcode357](https://gitlab.com/darkcode357)    | [acammackr7](https://keybase.io/acammackr7)        |
| [@KillerBean](https://gitlab.com/KillerBean)      | [bcoles](https://keybase.io/bcoles)                |

Note, keybase.io does **not require** your private key to prove your GitHub
identity. Actually sharing your private key with Keybase.io is a matter of
contention -- here's the usual argument [against][con-sharing], and here's one
thoughtful argument [for][pro-sharing].

As all Metasploit Framework committers are quite comfortable with the command
line, there should be no need to store your (encrypted) private key with a
third party. So, please don't, unless you have amazingly good reasons (and a great
local password).

# Tracking criteria

In order to get [@bcook-r7](https://github.com/bcook-r7) to track your key, you
alert him to its existence through some non-GitHub means, and verify your
GitHub username. That's all there is to it.

It would be sociable to track him (and everyone else on this list) back.
Tracking is essentially "trusting" and "verifying" -- see the much longer
discussion [here][tracking].

# Signing your commits and merges

Contributors are encouraged to sign commits, while Metasploit committers are required to sign their merge commits.  Note that the name and e-mail address must match the information on the signing key exactly.  To begin:

1. Generate a signing key, if you don't have one already, using your favorite PGP/GPG interface:

```
$ gpg --gen-key
gpg (GnuPG) 1.4.20; Copyright (C) 2015 Free Software Foundation, Inc.
This is free software: you are free to change and redistribute it.
There is NO WARRANTY, to the extent permitted by law.

Please select what kind of key you want:
   (1) RSA and RSA (default)
   (2) DSA and Elgamal
   (3) DSA (sign only)
   (4) RSA (sign only)
Your selection? 4
RSA keys may be between 1024 and 4096 bits long.
What keysize do you want? (2048) 
Requested keysize is 2048 bits
Please specify how long the key should be valid.
         0 = key does not expire
      <n>  = key expires in n days
      <n>w = key expires in n weeks
      <n>m = key expires in n months
      <n>y = key expires in n years
Key is valid for? (0) 1y
Key expires at Fri 20 Dec 2019 01:38:11 PM CST
Is this correct? (y/N) y

You need a user ID to identify your key; the software constructs the user ID
from the Real Name, Comment and Email Address in this form:
    "Heinrich Heine (Der Dichter) <heinrichh@duesseldorf.de>"

Real name: Dade Murphy
Email address: dmurphy@thegibson.example
Comment: 
You selected this USER-ID:
    "Dade Murphy <dmurphy@thegibson.example>"

Change (N)ame, (C)omment, (E)mail or (O)kay/(Q)uit? o
You need a Passphrase to protect your secret key.

Enter passphrase: [...]
```

2. Modify your `.git/config` file to enable signing commits and merges by default:

````
[user]
  name = Your Name
  email = your_email@example.com
  signingkey = DEADBEEF # Must match name and email exactly!
[alias]
  c = commit -S --edit
  m = merge -S --no-ff --edit
````

Using `git c` and `git m` from now on will sign every commit with your `DEADBEEF` key. However, note that rebasing or cherry-picking commits will change the commit hash, and therefore, unsign the commit -- to resign the most recent, use `git c --amend`.

[msf-committers]:https://github.com/rapid7/metasploit-framework/wiki/Committer-Rights
[pro-sharing]:https://filippo.io/on-keybase-dot-io-and-encrypted-private-key-sharing/
[con-sharing]:https://www.tbray.org/ongoing/When/201x/2014/03/19/Keybase#p-5
[tracking]:https://github.com/keybase/keybase-issues/issues/100