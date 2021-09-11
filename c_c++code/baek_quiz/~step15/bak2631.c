// https://www.acmicpc.net/problem/2631
// 줄세우기 LIS
#include <stdio.h>

int main(){
    int n;
    scanf("%d",&n);
    int *nums = (int*)malloc(sizeof(int)*n);
    for(int i=0; i<n;i++){
        scanf("%d",nums+i);
    }
    
}