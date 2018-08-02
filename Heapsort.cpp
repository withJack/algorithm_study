//2014004948_이승재_508

#include <stdio.h>


int Parent(int i)
{return i/2;}

//Left,Right is child index

int Left(int i)
{return 2*i;}

int Right(int i)
{return (2*i+1);};

void Swap(int *a, int *b)
{
	int tmp=*a;
	*a=*b;
	*b=tmp;
}


void Max_Heapify(int A[], int i, int length)
{
	int l,r,largest;
	l=Left(i);
	r=Right(i);

	if(l<=length && A[l]>A[i])
		largest=l;
	else
		largest=i;

	if(r<=length && A[r]>A[largest])
		largest = r;
	if(largest!=i)
	{
		Swap(&A[i],&A[largest]);	
		Max_Heapify(A,largest,length);
	}
}

void HeapSort(int A[],int length, int k)
{
	int i=length, size=length;
	for(;i>length-k;i--)
	{
		Swap(&A[1],&A[i]);
		size--;
		Max_Heapify(A,1,size);
		printf("%d ",A[i]);
	}
}

int main(void)
{
	int i,length,k;

	scanf("%d %d",&length,&k);

	int A[length+1];
	A[0]=0;

	for(i=1; i<=length;i++)
		scanf("%d",&A[i]);

	for(i=length/2;i>=1;i--)
		Max_Heapify(A,i,length);
	
	HeapSort(A,length,k);

	printf("\n");
	
	for(i=1;i<=length-k;i++)
		printf("%d ",A[i]);
}

