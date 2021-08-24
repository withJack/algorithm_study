#include <stdio.h>

void Print(int S[100][101], int i, int j)
{
	if(i==j)
		printf("%d ",i);
	else 
	{
		printf("( ");
		Print(S,i,S[i][j]);
		Print(S,S[i][j]+1,j);
		printf(") ");
	}
}


int main(void)
{

	int N;
	scanf("%d", &N);

	int P[N+2];

	for(int i=1; i<=N+1;i++)
		scanf("%d",&P[i]);
	
	//행렬은 N개 배열i=PixPi+1

	int M[N+1][N+1];
	int S[100][101];

	for(int i=1;i<=N;i++)
		M[i][i]=0;
	
	int j,q;
	for(int l=2;l<=N;l++)
		for(int i=1;i<=N-l+1;i++)
		{
			j=i+l-1;
			M[i][j]=999999;
			for(int k=i;k<=j-1;k++)
			{
				q=M[i][k]+M[k+1][j]+P[i]*P[k+1]*P[j+1];
				if(q<M[i][j])
				{
					M[i][j]=q;
					S[i][j]=k;
				}
			}
		}
	
	printf("%d\n",M[1][N]);
	
	Print(S,1,N);
}

