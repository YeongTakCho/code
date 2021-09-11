//https://www.acmicpc.net/problem/2156
//3개가 연속하지 않게 최대의 수의 합을 구하기
/* max select:
n:a  => a= (n/3)*2 + (n-(n/3)*3)
0:0
1:1 0
2:2 00

3:2 00 0
4:3 00 0 0
5:4 00 0 00

6:4 00 0 00 0
7:5 00 0 00 0 0
8:6 00 0 00 0 00

9:6 00 0 00 0 00 0
*/
//max_select= (n/3)*2 + (n-(n/3)*3)
#include <stdio.h>
#include <stdlib.h>
#define SETTING_NUM -100

//함수 작성 필요
int par_sum(int select_num, int* drink_amount,int n,int first,int second){
    if (first == SETTING_NUM){
        for(int i=0; i<=n-select_num;i++){
            par_sum(select_num -1, *drink_amount,n,i,SETTING_NUM);
        }
    }
    else if(second == SETTING_NUM){
        for(int i=first+1; i<=n-select_num+1;i++){
            par_sum(select_num-1,drink_amount,n,first,i);
        }
    }
    else{
        for(int i=second+1; i<=)
    }
    return big;
}
int main(){
    int n,max_select,biggest;
    int *amount;

    scanf("%d",&n);
    max_select = (n/3)*2 + (n-(n/3)*3);
    amount=(int*)malloc(sizeof(int)*n);
    for(int i=0; i<n; i++){
        scanf("%d",amount+i);
    }
    for(int i=1; i<=max_select;i++){
        int big;
        if(biggest < (big=par_sum(i,amount,n,SETTING_NUM,SETTING_NUM))){
            biggest = big;
        }
    }
    printf("%d",biggest);
}