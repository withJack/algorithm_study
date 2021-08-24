//2014004948_이승재_508

#include <stdio.h>
#include <cstdlib>

int length;

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


void Max_Heapify(int *A, int i)
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
		Max_Heapify(A,largest);
	}
}

int Extract_Max(int *A)
{
	int max =A[1];
	A[1] = A[length];
	(length)--;
	Max_Heapify(A, 1);
	A[length+1];
	return max;
}

void Increase_key(int *A,int i, int key)
{
	A[i] = key;
	if(i>1 && A[Parent(i)]>A[i])
		Max_Heapify(A,i);
	while(i>1 && A[Parent(i)]<A[i])
	{
		Swap(&A[i],&A[Parent(i)]);
		i= Parent(i);
	}
	
}

void Max_Insert(int *A,int key)
{
	length++;
	A[length] = 0;
	Increase_key(A,length,key);
}


int main(void)
{
	int i,option=1, key, index;
	int A[5000];
	int B[5000], count=0;
	while(option!=0)
	{
		scanf("%d",&option);
		switch(option)
		{
			case 0:
				for(i=0;i<count;i++)
					printf("%d ",B[i]);
				printf("\n");
				for(i=1;i<=length;i++)
					printf("%d ",A[i]);
				return 0;
			
			case 1:
				scanf("%d",&key);
				Max_Insert(A,key);
				
				break;
	
			case 2:
				B[count]=Extract_Max(A);
				count++;
				break;
			
			case 3:
				scanf("%d %d",&index,&key);
				Increase_key(A,index,key);
				break;
		}
	}
}

