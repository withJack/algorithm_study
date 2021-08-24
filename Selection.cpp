//2014004948_이승재_508

#include <stdio.h>

void S_Sort(int A[],int length,int step)
{
	int i=0;
	int j;
	int tmp;
	int min_index;

	for(;i<step;i++)
	{
		min_index = i;
		for(j=i+1; j<length;j++)
			if(A[min_index] >A[j])
				min_index = j;
	//swap
		tmp=A[min_index];
		A[min_index]=A[i];
		A[i] = tmp;
	}
}


int main (void)
{
	int length, step;
	int i=0;

	scanf("%d %d",&length, &step);
	
	int A[length];

	for(;i<length;i++)
		scanf("%d",&A[i]);

	S_Sort(A,length,step);
	
	i=0;
	for(;i<length;i++)
		printf("%d\n",A[i]);
}


