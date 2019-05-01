# QRGen

I've wrote this little script to generate generic Malformed QRCodes.
These urlcodes are useful if you want to test some QRCode scanner's parser or how the application handle QRCode data.
Down side of this tool: you need to manually scan codes with camera :(

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

