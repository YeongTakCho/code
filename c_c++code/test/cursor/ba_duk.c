//https://m.blog.naver.com/skssim/111983268

#include <stdio.h>

void main()
{
int i, j;
unsigned char a=0xa6;
unsigned char b[12];

for(i=1; i<12; i++)
{
b[i]=0xa0+i;        //0xa1부터  0xa11까지의 값을 순서대로 저장
}
        /*바둑판 첫번째 줄 출력하는 코드 */
printf("%c%c", a, b[3]);

for(i=0; i<20; i++)                   //20 열을 출력(실제로는 21열이 출력된다 - 양쪽에 반개씩 한열)
{
printf("%c%c", a, b[8]);
}
printf("%c%c", a, b[4]);
printf("\n");

        /* 바둑판 두번째 줄 부터 마지막 줄 전까지 같은 코드를 반복*/

for(i=0; i<20; i++)                 //20 행을 출력(실제로는 21열이 출력된다  -  양쪽에 반개씩 한행)
{
printf("%c%c", a, b[7]);
for(j=0; j<20; j++)        // 20열 출력(21열)
{
printf("%c%c", a, b[11]);
}

printf("%c%c", a, b[9]);
printf("\n");
}

        /* 바둑판 마지막 줄을 출력하는 코드 */

printf("%c%c", a, b[6]);

for(i=0; i<20; i++)               //20열을 출력(21열)
{
printf("%c%c", a, b[10]);
}
printf("%c%c", a, b[5]);
printf("\n");
}