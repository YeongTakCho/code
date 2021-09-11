//https://www.acmicpc.net/problem/1934
//최소공배수

#include <stdio.h>
#include <stdlib.h>
int LCM(int n,int m){ //n<m인 상황을 연출
    int l;
    int i=1;
    int num;
    if(m<n){
        l=m;
        m=n;
        n=l;
    }
    while(1){
        num=n*i;
        if(num-(num/m)*m==0){
            return num;
        }
        else i++;
    }
}
int main(){
    int n;
    int *nums;
    scanf("%d",&n);
    nums=(int*)malloc(sizeof(int)*n*2);
    for(int i=0; i<n*2;i++){
        scanf("%d",nums+i);
    }
    for(int i=0; i<n; i++){
        printf("%d\n",LCM(*(nums+i*2),*(nums+i*2+1)));
    }
    return 0;
}