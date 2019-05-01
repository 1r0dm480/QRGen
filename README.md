# QRGen ![img](https://img.shields.io/badge/version-v0.1-orange.svg?style=for-the-badge) ![img](https://img.shields.io/badge/python-v3.6+-green.svg?style=for-the-badge)

I've wrote this little script to generate generic Malformed QRCodes.
These qrcodes are useful if you want to test some QRCode scanner's parser or how the application handle QRCode data.<br>
Down side of this tool: you need to manually scan codes with camera :(

### Proof
![](demo.gif)

### Installation
What to you need:
- python3
- qrcode
- Pillow
- argparse

### Personalization
You can change the default wordlists to what you want :)

Order of wordlists group:
- SQL Injection
- XSS
- Command Injection
- Format String
- XXE
- String Fuzzing
- SSI Injection
- LFI/Directory Traversal
- custom passed with -w/--wordlist

