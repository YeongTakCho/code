//https://www.acmicpc.net/problem/1003
//피모나치 함수의 0과 1의 갯수
#include <stdio.h>
#include <stdlib.h>

void fibonacci(int num,int* fi_0, int* fi_1){
    if(num ==0){
        (*fi_0)++;
    }
    else if(num==1){
        (*fi_1)++;
    }
    else{
        fibonacci(num-1,fi_0,fi_1);
        fibonacci(num-2,fi_0,fi_1);
    }
}

// 아마 동적메모리 사용에서 오류난듯 + 포인터
int main(){
    int test_case;
    int fi_0=0, fi_1=0;
    int *p_fi_0=&fi_0, *p_fi_1=&fi_1;
    scanf("%d",&test_case);
    int *test_nums= (int*)malloc(sizeof(int)*test_case);
    for(int i=0; i<test_case;i++){
        scanf("%d",test_nums+i);
    }
    for(int i=0; i<test_case;i++){
        fibonacci(*(test_nums+i),p_fi_0,p_fi_1);
        printf("%d %d\n",*p_fi_0,*p_fi_1);
        *p_fi_0 =0, *p_fi_1=0;
    }
    free(test_nums);
}