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
    printf("%d���� ����\n",v);
    queue[rear] =v;
    rear++;

    while(front<rear){
        v = queue[front++];
		for (int i = 1; i <= n; i++)
		{
			// ���� v�� ���� i�� ������, ���� i�� �湮���� ���� ������ ���
			if (map[v][i] == 1 && !visit[i])
			{
				visit[i] = 1; // ���� i�� �湮�ߴٰ� ǥ��
				printf("%d���� %d�� �̵�\n", v, i);
				queue[rear++] = i; // ť�� i�� �����ϰ� �Ĵ��� 1 ������Ŵ
			}

    }

}