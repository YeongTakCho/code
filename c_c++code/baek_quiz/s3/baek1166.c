// https://www.acmicpc.net/problem/1166
// 문제가 이해 되지 않는다
#include <stdio.h>
#include <math.h>

int gcd(int a, int b){
    int gcdNum=0;
    int c;
    if (a>b){
        c=a,a=b,b=c;
    }
    for (int i=1; i<=a,i++){
        if(a%i==0 && b%i==0){
            gcdNum==i;
        }
    }
    return gcdNum;
}
int main(){
    int volume;
    int n,l,w,h;
    int gcdNum;
    scanf("%d",&n);
    scanf("%d",&l);
    scanf("%d",&w);
    scanf("%d",&h);
    gcdNum=gcd(gcd(l,w),h);
    


}