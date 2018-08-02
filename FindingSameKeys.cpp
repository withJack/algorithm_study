//2014004948_이승재_508

#include <stdio.h>

int Merge (int A[] , int p, int q, int r)
{
        int num1 = q-p+1;       //A[p...q]
        int num2 = r-q;         //A[q+1...r]
        int L[num1+1];          //left-side
        int R[num2+1];          //right-side
        int a,b;
	        for(a=0; a<num1;a++)
	                L[a]=A[p+a];            //copy first half
	        for(b=0; b<num2;b++)
	                R[b]=A[q+b+1];          //copy other half
	L[num1]=0;                      //consider lowest number is 0
        R[num2]=0;

	a=0,b=0;										
	for (int i=p; i<=r; i++)	       
	{
		if(L[a]>=R[b]) 
		{
			A[i]=L[a];
			a++;
		}
		else
		{
			A[i]=R[b];
			b++;
		}
		
	}

}

int Merge_Sort(int A[] ,int p, int r)
{
	int q;
	if(p<r)
	{
		q = (p+r)/2;
	//      printf("-%d-\n",q);
		Merge_Sort(A,p,q);
		Merge_Sort(A,q+1,r);
		Merge(A,p,q,r);
	}
}



int main(void)
{
	int N,M;
	int i,j=0,cnt=0;

	scanf("%d %d", &N, &M);

	int A[N];
	int B[M];


	for(i=0;i<N;i++)
		scanf("%d",&A[i]);
	for(i=0;i<M;i++)
		scanf("%d",&B[i]);

//printf("%d %d\n",A[N-1],B[M-1]);
	
	Merge_Sort(A,0,N-1);
	Merge_Sort(B,0,M-1);
	
//printf("%d %d\n",A[N-1],B[M-1]);
	i=N-1;
	j=M-1;

	while( i>=0 && j>=0 )
	{
		if(A[i]==B[j])
		{
			cnt++;
			i--;
			j--;
		}else if(A[i]<B[j])
		{
			i--;
		}else
			j--;
	}

	printf("%d\n",cnt);

	return 0;
}
