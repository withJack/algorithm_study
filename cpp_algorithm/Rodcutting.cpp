//2014004948_이승재_508

#include <stdio.h>

/*
int* RoD (int p[], int n)
{
	int r[n+1];
	int i=1,j=1;
	int q;

	r[0]=0;

	for(;j<=n;j++)
	{
		q=-1;
		for(;i<=j;i++)
		{
			if (q<p[i]+r[j-i])
				q= p[i]+r[j-i];
			r[j]=q;
		}
	}
	return r;
}
*/


int main()
{
	//int cnt=0;
	int N;
	int i=1,j=1,k=1;
	int q;
	scanf("%d", &N);
	
	int P[N+1];
	int R[N+1];
	int cnt[N+1];
	//int S[N+1];
	
	for(;k<=N;k++)
		scanf("%d",&P[k]);

	//R=RoD(P,N);
	//printf("%d\n",R[N]);
	P[0]=0;
	R[0]=0;
	cnt[0]=0;

	for(;j<=N;j++)
	{
		q=-1;
		for(i=1;i<=j;i++)
		{
			if (q<P[i]+R[j-i])
			{
				q= P[i]+R[j-i];
				cnt[j]=i;
			}
			R[j]=q;
		}
	}
	printf("%d\n",R[N]);
	
	while(N>0)
	{
		printf("%d ",cnt[N]);
		N=N-cnt[N];
	}
/*
	//printf("%d ", cnt[N]);

	
	//printf("%d ",cnt[N]);
	if(cnt[N] != 0 && cnt[N] != N)
		if(N-cnt[N]>cnt[N])
			printf("%d %d", cnt[N], N-cnt[N]);
		else
			printf("%d %d", N-cnt[N],cnt[N]);
	else if(cnt[N] == N)
		printf("%d", cnt[N]);
	else
		printf("%d", N-cnt[N]);
*/
	return 0;
}

