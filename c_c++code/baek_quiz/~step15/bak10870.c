//https://www.acmicpc.net/problem/10870

#include <stdio.h>

int run_pi(int i,int a, int b){
    if (i==1)
    {
        return b;
    }
    else{
        printf("%d ",b);
        return run_pi(i-1,b,a+b);
        }
}
int main(){
    int i;
    scanf("%d",&i);
    printf("%d",run_pi(i,0,1));
}