#include <stdio.h>
#include <stdlib.h>

typedef struct time
{
	int start;
	int finish;
}time;

int ctime = 0;
int back = 0;

void DFS_visit(int **adj, int *color, int N, int index, time *Time);
void DFS(int** adj,int *color, int N, time *Time)
{
	int i;
	for(i=1;i<=N;i++)
		if(color[i] == 0)
			DFS_visit(adj,color,N,i,Time);		
}


void DFS_visit(int **adj, int *color, int N, int index, time *Time)
{
	ctime++;
	Time[index].start = ctime;
	color[index] = 1;

	int i;
	for(i=1;i<=N;i++)
	{
		if(adj[index][i] == 1)
		{
			if(color[i] == 0)
				{DFS_visit(adj,color,N,i,Time);}
			else if(color[i] == 1)
				{back = 1;}
		}	
	}
	color[index] = 2;
	ctime++;
	Time[index].finish = ctime;
}

int main(void)
{
	int i,j,N;
	scanf("%d",&N);

	int** adj = (int **)malloc(sizeof(int *)*(N+1));
	
	for(i=1;i<=N;i++)
		adj[i] = (int *)calloc(1,sizeof(int)*(N+1));

	int* color =  (int *)calloc(1,sizeof(int)*(N+1));	//white =0; gray =1; black =2;

	time *Time = (time *)malloc(sizeof(time)*(N+1));

	int str, end;
	while(scanf("%d %d", &str, &end) != EOF)
		adj[str][end] = 1;
	
	DFS(adj,color,N,Time);
	
//	for(i=1;i<=N;i++)
//		printf("%d %d\n",Time[i].start,Time[i].finish);

	
	if(back == 1)
		printf("0\n");
	else
	{
		printf("1\n");

		int max=0;
		int idx;
		for(i=1;i<=N;i++)
		{
			for(j=1;j<=N;j++)	
				if(max < Time[j].finish)
				{
					max = Time[j].finish;
					idx = j;
				}
			printf("%d ",idx);
			Time[idx].finish = -1;
			max = 0;
		}
	}
	return 0;
}


