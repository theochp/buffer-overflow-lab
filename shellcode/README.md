# Setup
## Disable ASLR
```bash
echo "0" | sudo dd of=/proc/sys/kernel/randomize_va_space
```
Re-enable ASLR :
```bash
echo "2" | sudo dd of=/proc/sys/kernel/randomize_va_space
```

## Compile
```bash
make main
```

## Shellcode examples
[http://shell-storm.org/shellcode/](http://shell-storm.org/shellcode/)