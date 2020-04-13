#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <string.h>

void exploit() {
  printf("Succesfuly entered exploit function\n");
  system("/bin/sh");
}

void echo() {
  char passwd[20];

  printf("Type password\n");
  gets(passwd);

  if (strcmp("1234", passwd) == 0) {
    printf("Password correct\n");
    return;
  } else {
    exit(1);
  }
}

void main() {
  echo();
}
