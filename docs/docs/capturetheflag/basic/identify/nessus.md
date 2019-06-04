# NESSUS

# Basic Nessus scan:

```
nessus -q -x -T html <NESSUS SERVER IP ADDRESS> <NESSUS SERVER PORT 1241> <ADMIN ACCOUNT> <ADMIN>PASSWORD> <FILE WITH TARGETS>,txt <RESULTS FILENAME>.html
nessus [-vnh] [-c .refile] [-VJ [-T <format>]
```

# Batch-mode scan
```
nessus -q [-pPS] <HOST> <PORT> <USER NAME><PASSWORD> <targets-file> <result-file>
```

# Report conversion:
```
# nessus -i in. [nsrlnbe] -oout. [xmllnsrlnbelhtmlltxt]
```