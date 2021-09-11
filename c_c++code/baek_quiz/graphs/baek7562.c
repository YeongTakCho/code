//백준 7562 나이트의 이동 silver2

#include <stdio.h>
#include <stdlib.h>
int map[300][300];
int map_size[300][300];
int queue[90000];
int front, rear;
int move_num=0;
int I;
int move_x[8]={1,2,2,1,-1,-2,-2,-1};
int move_y[8]={2,1,-1,-2,-2,-1,-1,-2};

typedef struct xy{
    int x;
    int y;
}xy;
xy start,end;


void init_queue(){
    front=rear=0;
}
int isEnd(int x, int y){
    if(x == end.x && y==end.y){
        return 1;
    }
    return 0;
}
int inMap(int x, int y){
    if(x<I && y<I){
        return 1;
    }
    return 0;
}

void move(xy start){
    map[start.y][start.x]=move_num;
    //조건: 기존에 도착하지 않음, 맵 사이즈를 넘지 않음, 도착이 아님
    //조건에 맞음 -> 큐에 넣음 -> 8개를 검사 후 큐를 실행
    for(int i=0; i<8; i++){
        int x1= start.x+move_x[i], y1= start.y+move_y[i])
        if(isMap(x1, y1) && map[y1][x1]){
            xy isEndxy= {x1,y1};
            if(isEnd(isEndxy)){
                
            }
            queue[rear++]=
        }
        move_num++;
    }
}
int main(){
    int T;
    scanf("%d",&T);
    for(int repeat=0; repeat<T; T++){
        scanf("%d",I);
        for(int i=0; i<I; i++){
            for(int j=0; j<I; j++){
                map_size[i][j]=1;
            }
        }

        scanf("%d",&start.x);
        scanf("%d",&start.y);
        
        scanf("%d",&end.x);
        scanf("%d",&end.y);
        
        init_queue();
        move(start);

        for(int i=0; i<I; i++){
            for(int j=0; j<I; j++){
                map_size[i][j]=0;
            }
        }
    }
}