#include <stdio.h>

int main(){
    int n;
    scanf("%d",&n);
    int fibonacci_Store[51];
    fibonacci_Store[0]=1;
    fibonacci_Store[1]=1;
    for(int i=2; i<=n;i++){
        *(fibonacci_Store+i) = (*(fibonacci_Store+(i-2)) + *(fibonacci_Store+(i-1))+1)%1000000007;
    }
    printf("%d\n",(*(fibonacci_Store + n))%1000000007);
}