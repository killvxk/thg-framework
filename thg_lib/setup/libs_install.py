from os import system

database = [
        'cloudera-director-python-client cm-client cm-api crepo altuscli redis  ifxpy pymysql cx_Oracle psycopg2 pymongo ibm_db pyodbc  teradata mysql-connector mysql  neo4j-driver pyorient toad pyarrow  ']

network = [
        'beautifulsoup4 requests wget python-nmap GitPython nclib paramiko pyserial requests pysocks packaging pycurl ajpy pyopenssl dnspython  pysnmp pyasn1 pysmb  pysnmp']

aux = [
        'pytest mkdocs-bootstrap  filemagic  passlib hexdump  mako pyelftools capstone ropgadget pip tox rarfile pygments python-dateutil  psutil intervaltree unicorn pycrypto  IPy  mkdocs  future requests paramiko  pycryptodome distorm3']
print("install database")
for i in database:
        from os import system

        system("pip3 install " + i)
print("install network")
for i in network:
        from os import system

        system("pip3 install " + i)
print("install aux")
for i in aux:
        from os import system
        system("pip3 install "+i)
# system("pip3 install git+https://github.com/arthaud/python3-pwntools")
