#include<stdio.h>
#define MAX_STACK_SIZE 100
 
int stack[MAX_STACK_SIZE];
int top=-1;
 
int IsEmpty(){
    if(top<0)
        return 1;
    else
        return 0;
    }
int IsFull(){
    if(top>=MAX_STACK_SIZE-1)
        return 1;
    else
        return 0;
}
 
void push(int value){
    if(IsFull()==1)
        printf("������ ���� á���ϴ�.");
    else
        stack[++top]=value; 
}
 
int pop(){
    if(IsEmpty()==1)
        printf("������ ������ϴ�.");
    else 
        return stack[top--];
}
 
int main(){
    
    push(3);
    push(5);
    push(12);
    printf("%d ",pop());
    printf("%d ",pop());
    printf("%d ",pop());
 
    return 0;
}