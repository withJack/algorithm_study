#include <stdio.h>
/*
int Fastest(int l1[], int l2[], int a1[], int a2[], int t1[], int t2[], int e1, int e2, int x1, int x2, int N)
{
	int f1[N+1];
	int f2[N+1];
	int ff, ll;
	//int tf[2];

	f1[1] = e1+a1[1];
	f2[1] = e2+a2[1];

	for(int j=2; j<=N; j++)
	{
		if(f1[j-1] + a1[j] <= f2[j-1] + t2[j-1] + a1[j])
		{
			f1[j] = f1[j-1] + a1[j];
			l1[j] = 1;
		}
		else
		{
			f1[j] = f2[j-1] + t2[j-1] + a1[j];
			l1[j] = 2;
		}
		
		if(f2[j-1] + a2[j] <= f1[j-1] + t1[j-1] + a2[j])
		{
			f2[j] = f2[j-1] + a2[j];
			l2[j] = 2;
		}
		else
		{
			f1[j] = f1[j-1] +t1[j-1] + a2[j];
			l2[j] = 1;
		}
	}
	if(f1[N] + x1 <= f2[N] + x2)
	{
		ff = f1[N] + x1;
		ll = 1;
	}
	else 
	{
		ff = f2[N] +x2;
		ll = 2;
	}
	//tf[0] = ff;
	//tf[1] = ll;
	printf("%d\n",ff);
	return ll;
}
*/


int main()
{
//	int tf;

	int N;
	scanf("%d", &N);
	int a1[N+1];
	int a2[N+1];
	int t1[N];
	int t2[N];
	int l1[N+1];
	int l2[N+1];
	int e1,e2;


	scanf("%d %d", &e1, &e2);

	int x1,x2;
	scanf("%d %d", &x1, &x2);

	for(int i=1;i<=N;i++)
		scanf("%d", &a1[i]);
	for(int i=1;i<=N;i++)
		scanf("%d", &a2[i]);

	for(int i=1;i<N;i++)
		scanf("%d", &t1[i]);
	for(int i=1;i<N;i++)
		scanf("%d", &t2[i]);

//	tf = Fastest(l1, l2, a1, a2, t1, t2, e1, e2, x1, x2, N);
//////////////////////
	int f1[N+1];
	int f2[N+1];
	int ff, ll;
	//int tf[2];

	f1[1] = e1+a1[1];
	f2[1] = e2+a2[1];

	for(int j=2; j<=N; j++)
	{
		if((f1[j-1] + a1[j]) <= (f2[j-1] + t2[j-1] + a1[j]))
		{
			f1[j] = f1[j-1] + a1[j];
			l1[j] = 1;
		}
		else
		{
			f1[j] = f2[j-1] + t2[j-1] + a1[j];
			l1[j] = 2;
		}
		
		if((f2[j-1] + a2[j]) <= (f1[j-1] + t1[j-1] + a2[j]))
		{
			f2[j] = f2[j-1] + a2[j];
			l2[j] = 2;
		}
		else
		{
			f2[j] = f1[j-1] +t1[j-1] + a2[j];
			l2[j] = 1;
		}
	}
	if((f1[N] + x1) <= (f2[N] + x2))
	{
		ff = f1[N] + x1;
		ll = 1;
	}
	else 
	{
		ff = f2[N] +x2;
		ll = 2;
	}
	//tf[0] = ff;
	//tf[1] = ll;
	printf("%d\n",ff);
//////////////////////
	//int a=ll;
	int A[N+1];
	A[N] = ll;

	for(int i=N; i>=2; i--)
	{	
		if(A[i]==1)
			A[i-1]=l1[i];
		else
			A[i-1]=l2[i];
		
		//printf("%d %d\n", a, i-1);
	}

	for(int i=1; i<=N; i++)
		printf("%d %d\n",A[i],i);

	//printf("%d %d\n", tf[1], N);

	return 0;






}
