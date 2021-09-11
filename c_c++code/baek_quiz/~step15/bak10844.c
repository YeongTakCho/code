//https://www.acmicpc.net/problem/10844
/*
2자리 계단수
+a 01 ->1
10 12 ->2
21 23 ->2
32 34- >2
43 45 ->2
54 56 ->2
65 67 ->2
76 78 ->2
87 89 ->2
98    ->1
*/
//재귀함수 이용 ->  십의 자리의 숫자 갯수 -> 총 갯수
#include <stdio.h>

int ten2num(int ten){
    if (ten==0){
        return 1;
    }
    else if (ten ==9){
        return 1;
    }
    else{
        return 2;
    }  
}
int make_ten_par(int i,int n){
    if (n==2){
        return ten2num(i);
    }
    else if(i==0){
        return make_ten_par(i+1,n-1);
    }
    else if(i==9){
        return make_ten_par(i-1,n-1);
    }
    else{
        return make_ten_par(i-1,n-1)+make_ten_par(i+1,n-1);
    }
    
}
int make_ten(int n){
    if(n==1){
        return 9;
    }
    int sum=0;
    for(int i=1; i<=9; i++){
        sum= sum+ make_ten_par(i,n);
    }
    return sum;
}



int main(){
    int n;
    scanf("%d",&n);
    printf("%d",make_ten(n));
}