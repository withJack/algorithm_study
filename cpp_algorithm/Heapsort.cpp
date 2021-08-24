// Implementation on Heapsort with C language.
// Implemented by Jack.

#include <stdio.h>

// Parent() returns parent index.
int Parent(int i) { return i / 2; }

// Left(), Right() returns child index.
int Left(int i) { return 2 * i; }
int Right(int i) { return (2 * i + 1); };

// Simple function to swap the value of variables.
void Swap(int *a, int *b)
{
	int tmp = *a;
	*a = *b;
	*b = tmp;
}

// Check recursively the max-heap property for a single node from node i.
// And modifies the array A.
// Variable length is the legth of array A.
void Max_Heapify(int A[], int i, int length)
{
	int l, r, largest;
	l = Left(i);
	r = Right(i);

	if(l<=length && A[l]>A[i])
		largest = l;
	else
		largest = i;

	if(r<=length && A[r]>A[largest])
		largest = r;

	if(largest!=i)
	{
		Swap(&A[i], &A[largest]);
		Max_Heapify(A, largest, length);
	}
}

// From the last element, swap with the root of A.
// Use Max_Heapify() to organize the Heap.
// Recursively do this work excluding the last index of A.
void HeapSort(int A[], int length, int k)
{
	int i = length;
	int size = length;
	for(; i>length-k; i--)
	{
		Swap(&A[1], &A[i]);
		size--;
		Max_Heapify(A, 1, size);
		printf("%d ", A[i]);
	}
}

int main(void)
{
	int i, length, k;

	scanf("%d %d", &length, &k);

	int A[length+1];
	A[0] = 0;

	for(i=1; i<=length; i++)
		scanf("%d", &A[i]);

	for(i=length/2; i>=1; i--)
		Max_Heapify(A, i, length);

	HeapSort(A, length, k);

	printf("\n");

	for(i=1; i<=length-k; i++)
		printf("%d ", A[i]);
}

