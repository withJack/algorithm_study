//2014004948_이승재_508

#include <stdio.h>

void Counting_Sort(int *A, int length, int *C, int K)
{
	int i;
	//int C[K+1];

	for(i=0; i<=K; i++)
		C[i]=0;
	
	for(i=1; i<=length; i++)
		C[A[i]]=C[A[i]]+1;
	
	for(i=1; i<=K; i++)
		C[i] = C[i] + C[i-1];
/*	
	for(i=length; i>=1; i--)
	{
		B[C[A[i]]] = A[i];
		C[A[i]] = C[A[i]]-1;
	}
*/
}

int main(void)
{
	int N,M,K;
	int i,j,count=0;

	scanf("%d %d %d", &N, &M, &K);
//printf("%d %d %d", N,M,K);
	int A[N+1];
//	int B[N+1];
	int C[M+1];

	int tmp1[K];
	int tmp2[K];

	for(i=0; i<K; i++)
		scanf("%d %d",&tmp1[i], &tmp2[i]);
//printf(" %d \n", tmp1[1]);	
	for(i=1;i<=N;i++)
		scanf("%d",&A[i]);
	
	Counting_Sort(A,N,C,M);

	for(i=0; i<K; i++)
		printf("%d\n",(C[tmp2[i]]-C[tmp1[i]-1]));
	
/*
	for(i=0; i<K; i++)
	{
		for(j=1; j<=N; j++)
		{
			if(B[j]>=tmp1[i] && B[j]<=tmp2[i])
				count++;
		}		
		printf("%d\n",count);
		count=0;
	}
*/

	return 0;
}
