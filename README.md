# Buffer overflow exploit
## Required tools
- pip install pwntools
- install [pwngdb](https://github.com/pwndbg/pwndbg)

## Compile
```sh
gcc -o main main.c -fno-stack-protector -no-pie -std=c99
```