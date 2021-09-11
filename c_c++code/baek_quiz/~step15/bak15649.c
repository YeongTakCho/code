//https://www.acmicpc.net/problem/15649

// 1~n중 m개 중복없이 선택
#include <stdio.h>
#include <stdlib.h>

void n_m_fun(int n, int m,int *nums,int state){
    
    for(int i=1; i<=n;i++){
        for(int j=0; j<state;j++){
            if(*(nums+j) !=i){
                if(j== state-1){
                    *(nums+state-1)=i;
                    if(state == m){
                        for(int ii=0; ii<m; ii++){
                            printf("%d ",*(nums+ii));
                        }
                        printf("\n");
                    }
                    else{
                        n_m_fun(n,m,nums,state+1);
                    }
                }
                continue;
            }
            else{
                break;
            }
        }
    }
}

int main(){
    int n, m;
    int *nums;
    scanf("%d",&n);
    scanf("%d",&m);
    nums = (int*)malloc(sizeof(int)*m);
    n_m_fun(n,m,nums,1);

}
