#include <stdio.h>
#include <stdlib.h>

int find_pNum(int num){
    for(int i=2; i<num-1;i++){
        if(num%i==0){
            return 0;
        }
    }
    return 1;
}
int main(){
    int n;
    int multi_Num=1;
    scanf("%d",&n);
    int *nums = (int*)malloc(sizeof(int)*n);

    for(int i=0; i<n; i++){
        scanf("%d",nums+i);
        int num =find_pNum(*(nums+i));
        if(multi_Num%*(nums+i) !=0 && num ==1){
            multi_Num=multi_Num * (*(nums+i));
        }
    }
    if(multi_Num==1){
        printf("-1");
    }
    else{
        printf("%d",multi_Num);
    }
}