// https://www.acmicpc.net/problem/2580
#include <stdio.h>
#include <stdlib.h>

int find_garo_sero_square(int find_num,int state_num,int* cells){
    int garo= state_num - ((state_num)/9)*9;
    int sero= state_num/9;
    for(int i=0; i<9; i++){
        if(*(cells+9*sero+i)==find_num){
            return 1; //존재
        }
        if(*(cells+9*i+garo)==find_num){
            return 1;
        }
    }
    for(int i=(garo/3)*3; i<(garo/3)*3+3;i++){
        for(int j=(sero/3)*3; j<(sero/3)*3+3; j++){
            if(*(cells+i+j*9)==find_num){
                return 1;
            }
        }
    }
    return 0; //존재 x
}

// stoku 함수 - 수정필요
void stoku(int* cells,int* mark,int num){
    if(*(mark+num)!=0){
        if(num ==80){
            printf("\n");
            for(int j=0; j<81; j++){
                printf("%d",*(cells+j));
                if(((j+1)-((j+1)/9)*9)==0){
                    printf("\n");
                }    
            }
        }
        stoku(cells,mark,num+1);
    }
    else{
        for(int i=1; i<=9; i++){
            if(find_garo_sero_square(i,num,cells)==0){
                *(cells+num)=i;
                printf("cells[%d]= %d\n",num,i);
                if(num ==80){
                    printf("\n");
                    for(int j=0; j<81; j++){
                        printf("%d",*(cells+j));
                        if(((j+1)-((j+1)/9)*9)==0){
                            printf("\n");
                        }    
                     }
                }
                stoku(cells, mark,num+1);
            }
        }
        *(cells+num)=0;
    }
}


int main(){
    int cells[81];
    int mark[81];
    
    
    for(int i=0; i<81; i++){
        scanf("%d",(cells+i));
    }
    

    for(int i=0; i<81; i++){
        printf("%d",*(cells+i));
        if(((i+1)-((i+1)/9)*9)==0){
            printf("\n");
        }
    }
    //marking
    for(int i=0; i<81; i++){
        if(*(cells+i)==0){
            *(mark+i)=0;
        }
        else{
            *(mark+i)=1;
        }
    }
    //재귀함수
    stoku(cells,mark,0);

    printf("\n");

    
}