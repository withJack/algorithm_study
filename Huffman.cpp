#include <stdio.h>
#include <stdlib.h>

int Parent(int i)
{return i/2;}

int Left(int i)
{return 2*i;}

int Right(int i)
{return 2*i+1;}

void Swap(int *a, int *b)
{
	int tmp = *a;
	*a=*b;
	*b=tmp;
}

void MinHeapify(int A[], int i, int length)
{
	int l,r,smallest;
	l=Left(i);
	r=Right(i);
	
	if(l<=length && A[l]<A[i])
		smallest = l;
	else
		smallest = i;
	if(r<=length && A[r]<A[smallest])
		smallest =r;
	if(smallest != i)
	{
		Swap(&A[i], &A[smallest]);
		MinHeapify(A,smallest,length);
	}
}

void Build_Min(int A[], int length)
{
	for(int i=length/2; i>=1; i--)
		MinHeapify(A,i,length);
}

int ExtractMin(int A[], int length)
{
	int min = A[1];
	A[1] = A[length];

	A[length] = 0;

	length--;
	MinHeapify(A,1,length);
 
	return min;
}

void Increase_key(int A[], int i, int key, int length)
{
	A[i] = key;
	if(i>1 && A[Parent(i)]<A[i])
		MinHeapify(A,i,length);
	while(i>1 && A[Parent(i)]>A[i])
	{
		Swap(&A[i], &A[Parent(i)]);
		i =Parent(i);
	}
}
void Min_Insert(int A[], int key, int length)
{
	length++;
	A[length] = 999999;
	Increase_key(A,length,key,length);
}

int main(void)
{
	int N;
	scanf("%d",&N);
	
	int Huff[2*N];
	char A[5];
	int total;
	
	for(int i=1; i<=N; i++)
	{
		scanf("%s", A);
		scanf("%d", &Huff[i]);
	}
	
	scanf("%d", &total);
	int count=0;
	int fixedN = N-1;
	while((fixedN/=2)>=1)
		count++;
	printf("%d\n",total*(count+1));		//fixed-length coding
	
	Build_Min(Huff,N);
	
	int Heaplength=N;
	int a=1;
	int HuffmanN=0;

	while(Heaplength != 0)
	{
		Huff[2*N-a] = ExtractMin(Huff,Heaplength);
		Heaplength--;
		HuffmanN += Huff[2*N-a];
		if(Heaplength == 0)
			break;

		Huff[2*N-a-1] = ExtractMin(Huff,Heaplength);
		Heaplength--;
		HuffmanN += Huff[2*N-a-1];
		
		Min_Insert(Huff,Huff[2*N-a]+Huff[2*N-a-1],Heaplength);
//		Huff[Heaplength+1] = Huff[2*N-a] + Huff[2*N-a-1];
//		*(Huff[Heaplength+1].letter) = NULL;
		Heaplength++;
//		Build_Min(Huff,Heaplength);
		a=a+2;
	} 

//	for(int i=1;i<=2*N-1;i++)
//		printf("%d\n", Huff[i]);

	printf("%d\n",HuffmanN-total);

	return 0;
}


