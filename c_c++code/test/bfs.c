#include <stdio.h>

int n;
int rear=0, front=0;
int map[30][30],queue[30],visit[30];

void BFS(int n);

int main(){
    int start;
    int v1,v2;
    scanf("%d%d",&n,&start);
    while(1){
        scanf("%d%d",&v1,&v2);
        if(v1 ==-1 && v2 ==-1)break;
        map[v1][v2]=map[v2][v1]=-1;
    }
    BFS(start);
    return 0;
}

void BFS(int v){
    visit[v]=1;
    printf("%d에서 시작\n",v);
    queue[rear] =v;
    rear++;

    while(front<rear){
        v = queue[front++];
		for (int i = 1; i <= n; i++)
		{
			// 정점 v와 정점 i가 만나고, 정점 i를 방문하지 않은 상태일 경우
			if (map[v][i] == 1 && !visit[i])
			{
				visit[i] = 1; // 정점 i를 방문했다고 표시
				printf("%d에서 %d로 이동\n", v, i);
				queue[rear++] = i; // 큐에 i를 삽입하고 후단을 1 증가시킴
			}

    }

}