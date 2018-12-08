# HEX CONVERSION
## Convert from hex to decimal in Windows:
C:\> set /a 0xff
PS C:\> 0xff
## Other Basic Math in Windows:
C:\> set /a 1+2
C:\> set /a 3*(9/4)
C:\> set /a (2*5)/2
C:\> set /a "32>>3"
## Decode Base64 text in a file:
C:\> certutil -decode <BASE64<DECODED FILE NAME>

# ENCODED

## Decode XOR and search for http:
```
Ref,https://blog.didierstevens.com/programs/xorsearch/
C:\> xorsearch,exe -i -s <INPUT FILE NAME> http
```
## Convert from hex to decimal in Linux:
```
echo u0xff"lwcalc -d
= 255
```
## Convert from decimal to hex in Linux:
```
$ echo u25s"1wcalc -h
= 0xff
```
## Decode HTML Strings:
```
PS C:\> Add-Type -AssemblyName System.Web
PS C:\>[System.Uri] ::UnescapeDataString("HTTP%3a%2f%2fHello%20World.com")
HTTP://Hello World.com
```
