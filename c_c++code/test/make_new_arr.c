#include <stdio.h>
//fail
int main(){
    int arr[3]={1,2,3};
    for(int i=0; i<3; i++){
        printf("1. %d\n",arr[i]);
    }
    arr={0,};
    for(int i=0; i<3; i++){
        printf("1. %d\n",arr[i]);
    }

}