//2014004948_이승재_508

#include <stdio.h>

int Merge (int A[] , int p, int q, int r)
{
	int num1 = q-p+1;	//A[p...q]
	int num2 = r-q;		//A[q+1...r]
	int L[num1+1];		//left-side
	int R[num2+1];		//right-side
	int a,b;
	for(a=0; a<num1;a++)
		L[a]=A[p+a];		//copy first half
	for(b=0; b<num2;b++)
		R[b]=A[q+b+1];		//copy other half
	
	L[num1]=0;			//consider lowest number is 0
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
	//	printf("-%d-\n",q);
		Merge_Sort(A,p,q);
		Merge_Sort(A,q+1,r);
		Merge(A,p,q,r);
	}

}


int main (void)
{
	int length=0;

//	printf("Merge Sort\n");

	scanf("%d",&length);

	int A[length];

	for(int i=0; i<length;i++)
		scanf("%d",&A[i]);
	
	Merge_Sort(A,0,length-1);

	for(int i=0; i<length;i++)
		printf("%d\n",A[i]);
	
}
