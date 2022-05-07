#include <stdio.h>

int main(){
    char input[] = {'A','B','C','D','D','C','D','E','A'};
    char newinput[]= input;
    for (int i=0; i<sizeof(newinput)/sizeof(newinput[0]); i++){
        printf("%c",newinput[i]);
    }
}