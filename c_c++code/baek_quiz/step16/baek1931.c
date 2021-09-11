//https://www.acmicpc.net/problem/1931
//회의실 배정
//참고: https://www.zerocho.com/category/Algorithm/post/584ba5c9580277001862f188
#include <stdio.h>
#include <stdlib.h>

int meeting_set(int n, int *meetings){

    for(int i=0;i<n;i++){
        if(마지막일 경우){
            최대 값을 반환
        }
        else{
            if(자리가 겹치지 않을 경우){
                meeting_set(int n-(i+1),meetings+((i+1)*2))
            }
            else{
                다음 반복문으로 이동
            }
        }
    }
}
int main(){
    int n;
    scanf("%d",&n);
    int *meetings=(int*)malloc(sizeof(int)*n*2);
    for(int i=0; i<n*2; i++){
        scanf("%d",meetings+i);
    }
    printf("%d",meeting_set(n,meetings));
}