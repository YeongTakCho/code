//https://www.acmicpc.net/problem/2798
#include <stdio.h>
#include <stdlib.h>

int main(){
    int count, max;
    int closest=0, x, y, z;
    int sum_num;
    int *nums;
    scanf("%d %d",&count,&max);
    if (count<3 || count>100){
        if(max<10 || max >300000){
            printf("count and max are wrong");
            return 0;
        }
        else{
            printf("count is wrong");
            return 0;
        }
    }
    else if(max<0 || max >300000){
        printf("max is wrong");
        return 0;
    }
    
    nums=(int*)malloc(sizeof(int)*count);

    for(int i=0; i<count;i++){
        scanf("%d",(nums+i));
    }
    
    
    for(int i=0; i<count; i++){
        printf("%d ",*(nums+i));
    }
    printf("\n");
    for(x=0; x<count-2; x++){
        for(y=x+1;y<count-1;y++){
            for(z=x+2;z<count;z++){
                sum_num=*(nums+x)+*(nums+y)+*(nums+z);
                printf("%d = %d + %d + %d\n",sum_num,*(nums+x),*(nums+y),*(nums+z));
                if(sum_num> closest && sum_num<=max){
                    closest = sum_num;
                }
            }
        }
    }
    printf("%d",closest);
}