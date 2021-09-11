//s2
#include <stdio.h>
#include <stdlib.h>

int *nums, *nums_store;
int Length;
int total=0;
int x_Max(int y);
int y_Max(int x);
int f_state(int x, int y);
void Jump(int x, int y);

int main(){
    scanf("%d",&Length);
    nums=(int*)malloc(sizeof(int)*Length*Length);
    nums_store = (int*)malloc(sizeof(int)*Length*Length);

    for(int i=0; i<Length*Length;i++){
        scanf("%d",nums+i);
    }
    Jump(0,0);
    printf("%d",total);
}


void Jump( int x, int y){
    if(x==Length-1 && y == Length-1){
        total++;
    }
    else{
        int x1=x,y1=y;
        int state=x+y*Length;
        int x_max=x_Max(y);
        int y_max=y_Max(x);
        if(f_state(x1= x+*(nums+state),y) <=x_max){
            Jump(x1,y);
        }
        if(f_state(x,(y1 = y+*(nums+state)))<=y_max){
            Jump(x,y1);
        }
    }
}

int f_state(int x, int y){
    return x+ y*Length;
}
int x_Max(int y){
    return (y + 1)*Length -1;
}
int y_Max(int x){
    return (Length-1)*Length +x;
}