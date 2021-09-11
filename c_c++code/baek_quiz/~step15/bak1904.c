//https://www.acmicpc.net/problem/1904
/*
           000000- >1

10000 ->3  110000 ->6
00100      100100
00001      100001
           001100
           001001
11100 ->4  000011
11001      
10011      111100 ->5
00111      111001
           110011
11111 ->1  100111
           001111

           111111 ->1
->n(6) 13 = n(5) 8+ n(4) 5
n(1)= 1, n(2)=2 ... =>피모나치수열
*/

#include <stdio.h>

int run_fi(int num,int* sum){
    if(num ==1){
        (*sum)=(*sum)+1;
    }
    else if(num==2){
        (*sum)=(*sum)+2;
    }
    else{
        run_fi(num-1,sum);
        run_fi(num-2,sum);
    }
}
int main(){
    int num;
    int sum=0;
    int *p_sum=&sum;
    scanf("%d",&num);
    run_fi(num,p_sum);
    printf("%d",sum-(sum/15746)*15746);


}
