//https://www.acmicpc.net/problem/2750
#include <stdio.h>
#include <stdlib.h>
int main(){
    int n, before_num=0,current_num=1000;
    scanf("%d",&n);
    int *nums = (int*)malloc(sizeof(int)*n);
    for(int i=0; i<n; i++){
        scanf("%d",nums+i);
    }
    for(int i=0; i<n;i++){
        for(int j=0; j<n; j++){
            if(*(nums+j)>before_num && *(nums+j)<current_num){
                current_num = *(nums+j);
            }
        }
        printf("%d\n",current_num);
        before_num = current_num;
        current_num = 1000;
    }
}