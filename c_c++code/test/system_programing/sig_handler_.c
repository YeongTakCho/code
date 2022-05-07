#include <stdio.h>
#include <unistd.h>
#include <stdlib.h>
#include <sys/wait.h>
#include <signal.h>

void sig_handler(int signum){
    printf("signal handler started\n");
    for(int i=1; i<=5; i++){
        printf("%d.. ", i);
        sleep(1);
    } printf("\n");
    printf("signal handler ended\n");
    sleep(1);
    printf("restart\n");
}

int main(void){
    signal(SIGALRM,sig_handler);
    printf("signal halder for SIGALRM registered ... \n");

    kill(getpid(), SIGALRM);
    printf("continue processing...\n");
    return 0;
}