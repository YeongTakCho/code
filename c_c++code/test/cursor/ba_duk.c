//https://m.blog.naver.com/skssim/111983268

#include <stdio.h>

void main()
{
int i, j;
unsigned char a=0xa6;
unsigned char b[12];

for(i=1; i<12; i++)
{
b[i]=0xa0+i;        //0xa1����  0xa11������ ���� ������� ����
}
        /*�ٵ��� ù��° �� ����ϴ� �ڵ� */
printf("%c%c", a, b[3]);

for(i=0; i<20; i++)                   //20 ���� ���(�����δ� 21���� ��µȴ� - ���ʿ� �ݰ��� �ѿ�)
{
printf("%c%c", a, b[8]);
}
printf("%c%c", a, b[4]);
printf("\n");

        /* �ٵ��� �ι�° �� ���� ������ �� ������ ���� �ڵ带 �ݺ�*/

for(i=0; i<20; i++)                 //20 ���� ���(�����δ� 21���� ��µȴ�  -  ���ʿ� �ݰ��� ����)
{
printf("%c%c", a, b[7]);
for(j=0; j<20; j++)        // 20�� ���(21��)
{
printf("%c%c", a, b[11]);
}

printf("%c%c", a, b[9]);
printf("\n");
}

        /* �ٵ��� ������ ���� ����ϴ� �ڵ� */

printf("%c%c", a, b[6]);

for(i=0; i<20; i++)               //20���� ���(21��)
{
printf("%c%c", a, b[10]);
}
printf("%c%c", a, b[5]);
printf("\n");
}