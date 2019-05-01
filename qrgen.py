#!/usr/bin/python3
# -*- coding: utf-8 *-*
import qrcode
import subprocess
import sys
import argparse
from PIL import Image
qr_version="0.1"
banner='''
  e88 88e   888 88e    e88'Y88
 d888 888b  888 888D  d888  'Y   ,e e,  888 8e
C8888 8888D 888 88"  C8888 eeee d88 88b 888 88b
 Y888 888P  888 b,    Y888 888P 888   , 888 888
  "88 88"   888 88b,   "88 88"   "YeeP" 888 888
      b
      8b,    {}'''.format("QRGen ~ v0.1 ~ by h0nus\n")
print(banner)
#print('Tool to generate Malformed QRCodes for fuzzing QRCode parsers/reader\n')
parser = argparse.ArgumentParser(description="Tool to generate Malformed QRCodes for fuzzing QRCode parsers/reader",
                                 usage='''qrgen.py -l [number]\nusage: qrgen.py -w [/path/to/custom/wordlist]\n\nPayload lists:
0 : SQL Injections
1 : XSS
2 : Command Injection
3 : Format String
4 : XXE
5 : String Fuzzing
6 : SSI Injection
7 : LFI / Directory Traversal''',
epilog="Pay attention everywhere, even in the dumbest spot")
sgroup = parser.add_argument_group("Options for QRGen")
sgroup.add_argument("--list","-l",type=int,help="Set wordlist to use",choices=[0,1,2,3,4,5,6,7])
sgroup.add_argument("--wordlist","-w",type=str,default=None,help="Use a custom wordlist")

options = parser.parse_args()

if len(sys.argv) == 1:
    parser.print_help()
    sys.exit(1)

lists = ['words/sqli','words/xss.txt','words/cmdinj','words/formatstr.txt','words/xxe','words/strfuzz','words/ssi','words/lfi']
try:
    cmd= subprocess.check_output(['mkdir','genqr'],stderr=subprocess.STDOUT)
    print("Payload path generated..")
except:
    print("Payload path exist, continuing...")
    pass
try:
    cmd = subprocess.check_output(['rm', 'genqr/*'],stderr=subprocess.STDOUT)
    print("Clearing QR payloads dir..")
except:
    print("Path already cleared or deleted..")
    pass
payloads = []
if options.list:
    z = options.list
    payloads = open(lists[z]).readlines()
elif options.wordlist:
    z = options.wordlist
    payloads = open(str(z)).readlines()
i = 0
while i < len(payloads):
    payloads[i] = payloads[i].strip()
    i+=1
i=0
while i < len(payloads):
    img = qrcode.make(payloads[i])
    img.save("genqr/payload-{}.png".format(i))
    i+=1
print("Generated {} payloads!".format(len(payloads)))
Image.open("genqr/payload-{}.png".format(i-1)).show()
print("Opening last generated payload...")
print("Thanks for using QRGen, made by H0nus..")
