#include<stdio.h>

int main()
{
  FILE *fp;

  fp = fopen("test.txt", "w");

  if(fp == NULL){
    printf("���Ͽ��� ����\n");
  } else {
    printf("���Ͽ��� ����\n");
  }
  
  fclose(fp);

  return 0;
}