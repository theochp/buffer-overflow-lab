main: main.c
	gcc -o main main.c -fno-stack-protector -no-pie
