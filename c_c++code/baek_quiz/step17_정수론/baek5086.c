//https://www.acmicpc.net/problem/5086
//배수와 약수

#include <stdio.h>
#include <stdlib.h>

typedef struct NODE
{
    struct NODE *next;
    int data;
}NODE;
int find_multiple(int n, int m){
    if((m-(m/n)*n)==0){
        return 0;
    }
    else if(n-(n/m)*m==0){
        return 1;
    }
    else{
        return 2;
    }
}
int main(){
    int n, m;
    const char *s[3] = {"factor","multiple","neither"};
    NODE *head = NULL;
    NODE *prev, *p;


    while(1){
        scanf("%d",&n);
        getchar(); //버퍼제거
        scanf("%d",&m);
        getchar();
        printf("%d, %d\n",n,m);
        if(n ==0 && m ==0){
            break;
        }
        else{
            p=(NODE*)malloc(sizeof(NODE));
            if(head == NULL){
                head=p;
            }
            else{
                prev->next=p;
            }
            printf("%d\n",p->data = find_multiple(n,m));
        }
    }
    p=head;
    while(p==NULL){
        printf("%s",s[p->data]);
        p=p->next;
    }
    return 0;
}