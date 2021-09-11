//silver2 양배추
#include <stdio.h>
#include <stdlib.h>
typedef struct State{
    int x;
    int y;
}State;

int map[50][50];
int T,M,N,K;
//가로: M 세로 :N 야채의 수:K
int web(int x, int y);

int main(){
    scanf("%d",&T);
    int warm=0;
    int warms[50],w=0;
    for(int repeat=0; repeat<T;repeat++){
        scanf("%d",&M);
        scanf("%d",&N);
        scanf("%d",&K);
        State *state = (State*)malloc(sizeof(State)*K);
        for(int i=0; i<K;i++){
            int x, y;
            scanf("%d",&x);
            scanf("%d",&y);
            map[y][x]=1;
            (state+i)->x=x;
            (state+i)->y=y;
        }
        for(int i=0; i<K;i++){
            int x=(state+i)->x;
            int y=(state+i)->y;
            warm += web(x,y);
        }
        warms[w]=warm;
        w++;
        warm=0;
        free(state);
    }
    for(int i=0; i<w; i++){
        printf("%d\n",warms[i]);
    }
}

int web(int x, int y){ //return 0 ( no warm ) or 1 ( exzist warm )
    if(map[y][x]==0){
        return 0; //no vegetable
    }
    else{
        map[y][x]=0;
        //up
        if(y-1>=0){
            web(x,y-1);
        }
        //left
        if(x-1>=0){
            web(x-1,y);
        }
        //right
        if(x+1<M){
            web(x+1,y);
        }
        //down
        if(y+1<N){
            web(x,y+1);
        }
        return 1;
    }
    
}