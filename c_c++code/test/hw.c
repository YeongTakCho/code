#include <stdio.h>
#include <unistd.h>
#include <stdlib.h>
#include <sys/wait.h>

void fork1(){
    int N=100;

    pid_t pid[N];
    int i, child_status;
    for(i=0; i<N; i++){
        if((pid[i] = fork()) == 0)
            exit(100+i);
    }
    for(i=0; i<N; i++){
        pid_t wpid = waitpid(pid[i],&child_status,0);
        if(WIFEXITED(child_status)){
            printf("%d, %d\n", wpid, WEXITSTATUS(child_status));

        }q
        else{
            printf("%d \n",wpid);
        }
    }
}

int main(){
    fork1();
}