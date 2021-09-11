// https://www.acmicpc.net/problem/11047
//?èô?†Ñ 0 
//easy
#include <stdio.h>
#include <stdlib.h>

int main(){
    int coin_kinds, money;
    int *coins;
    int total_coin=0;
    scanf("%d",&coin_kinds);
    scanf("%d",&money);
    coins=(int*)malloc(sizeof(int)*coin_kinds);
    for(int i=0; i<coin_kinds;i++){
        scanf("%d",coins+i);
    }
    for(int i=coin_kinds; i>=1;i--){
        while(money>=*(coins+i-1)){
            money=money-*(coins+i-1);
            total_coin++;
        }
    }
    printf("%d",total_coin);
}
