//https://www.acmicpc.net/problem/2981
//검문. 나머지가 같은 수 찾기

#include <stdio.h>
#include <stdlib.h>

int main(){
    int n;
    int minimum=1000000000;
    scanf("%d",&n);
    int *nums=(int*)malloc(sizeof(int)*n);
    for(int i=0; i<n; i++)){
        scanf("%d",nums+i);
        if(*(nums+i)<minimun){
            minimum=*(nums+i);
        }
    }
    
}