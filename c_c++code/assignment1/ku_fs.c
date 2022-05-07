// command: ./ku_fs str i    
// str: substring to find
// i: number of parallel processes (>0)
// argv[1]: str, argv[2]: i
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <sys/types.h>
#include <unistd.h>
#include <sys/ipc.h>
#include <sys/msg.h>
#include <sys/wait.h>
#include "sample.h"
//#include <ku_fs_input.h> //code for submit

void bubble_sort(int arr[], int count)    
{
    int temp;

    for (int i = 0; i < count; i++)   
    {
        for (int j = 0; j < count - 1; j++)   
        {
            if (arr[j] > arr[j + 1])          
            {                                 
                temp = arr[j];
                arr[j] = arr[j + 1];
                arr[j + 1] = temp;            
            }
        }
    }
}

int main(int argc, char* argv[]){
    int  maxiter= (MAXS- strlen(argv[1]));
    int cNum = (MAXS - strlen(argv[1])) / (float)atoi(argv[2])+0.999; //one process check cNum of char in input
    int max_id=0, child_status;
    int arrived_msg[1000];
    key_t ipckey;
    int mqdes;
    size_t buf_len;

    struct{
        int value;
    }mymsg;

    buf_len = sizeof(mymsg.value);
    ipckey = ftok("./tmp/foo", 1946);
    mqdes = msgget(ipckey, IPC_CREAT|0600);

    if( mqdes < 0 ){
        perror("msgget()");
        exit(0);
    }

    for (int cnt=0; cnt<atoi(argv[2]); cnt++){
        if(fork() ==0){
            int send_num=0;
            printf("fork %d is start \n" ,cnt);
            for(int i= cnt * cNum; i< (cnt+1) * cNum; i++){
                if (i > maxiter) continue;

                if (input[i] == argv[1][0]){
                    int k =0;
                    for (int j=1; j< strlen(argv[1]); j++){
                        if(input[i+j] != argv[1][j]){
                            k= 1; j= strlen(argv[1]);
                        }
                    }
                    if (k ==0){
                        send_num+=1;
                        mymsg.value = i;
                        printf("message: %d\n", i);
                        if( msgsnd(mqdes, &mymsg, buf_len, 0) == -1 ){
                            perror("msgsnd()");
                            exit(0);
                        }
                    }
                }
            }
            exit(send_num);
        }
    }
    for(int i=0; i<atoi(argv[2]); i++){
        pid_t wpid= wait(&child_status);
        max_id += WEXITSTATUS(child_status);
        printf("child terminated with exit status %d\n",WEXITSTATUS(child_status));
    }
    printf("max_id : %d\n",max_id);
    for(int i=0; i<max_id; i++){
        if( msgrcv(mqdes, &mymsg, buf_len, i+1, 0) == -1 ){
                perror("msgrcv()");
                exit(0);
            }
        else{
            arrived_msg[i]= mymsg.value;
            printf("msg recived\n");
        }
           
    }
    
    bubble_sort(arrived_msg,sizeof(int) * max_id);

    for(int i=0; i<max_id;i++){
        printf("%d\n",arrived_msg[i]);
    }
}