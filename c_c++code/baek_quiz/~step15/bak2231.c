//https://www.acmicpc.net/problem/2231
#include <stdio.h>

int particular_sum(int number){
    int sum=number;
    while(number !=0){
        sum=sum + (number-(number/10)*10);
        number = number/10;
    }
        return sum;
}
int main(){
    int num,sum;
    int i;
    scanf("%d",&num);
    if(num<1 || num>1000000){
        printf("num is too big or small");
        return 0;
    }
    for(i=1; i<=num; i++){
        if(particular_sum(i) == num){
            break;
        }
        if(i == num){
            printf("no such number");
            break;
        }
    }
    printf("%d",i);


}