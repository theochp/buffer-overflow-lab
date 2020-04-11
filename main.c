#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <string.h>

void exploit() {
  system("/bin/sh");
}

void echo() {
  printf("Password?\n");
  char passwd[20];
  gets(passwd);

  if (strcmp("1234", passwd) == 0) {
    printf("In\n");
    return;
  } else {
    exit(1);
  }
}

void main() {
  echo();
}
