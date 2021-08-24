//2014004948_이승재_508

#include <stdio.h>

int main(void)
{
	int length=0;
	int key=0;
	int i=0,j=0;

//	printf("insertion.cpp\n");
	scanf("%d",&length);

	int A[length];
	
	for(int k=0; k<length;k++)
	{
		scanf("%d",&A[k]);
	}

	// array set. sorting start.

	for(i=1; i<length;i++)
	{
		key = A[i];
		j=i-1;
		while(j>=0 && A[j]<key)
		{
			A[j+1]=A[j];
			j=j-1;
		}
		A[j+1]=key;
	}

	for(int l=0; l<length; l++)
		printf("%d\n",A[l]);

	return 0;
}

