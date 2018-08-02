#include <stdio.h>

void Print(int C[][501], char A[], int Alength, int Blength)
{
	if(Alength==0 || Blength==0)
		return;
	if(C[Alength][Blength] == 3)
	{
		Print(C,A,Alength-1,Blength-1);
		printf("%c",A[Alength]);
	}
	else if(C[Alength][Blength] == 2)
		Print(C,A,Alength-1,Blength);
	else
		Print(C,A,Alength,Blength-1);
}

int main(void)
{
	char A[500];
	char B[500];
	int Alength=0;
	int Blength=0;
	char tmp;

	while((tmp = getchar()) != '\n' && tmp != EOF)
	{
		A[Alength+1]=tmp;
		Alength++;
	}

	while((tmp = getchar()) != '\n' && tmp !=EOF)
	{
		B[Blength+1] = tmp;
		Blength++;
	}
/*
	for(int i=1; i<5;i++)
	{
		printf("%c ",A[i]);
		printf("%c\n",B[i]);
	}
*/
	int m,n;

	if(Alength>=Blength)
	{
		n=Alength;		//x axis
		m=Blength;		//y axis	x-axis is longer
	}else
	{
		n=Blength;
		m=Alength;
	}
  
	int C[m+1][501];	//arrows	left:1 up:2 diagnal:3 
	int D[m+1][n+1];	//numbers

	for(int i=1; i<=m;i++)
		D[i][0]=0;
	for(int i=1; i<=n;i++)
		D[0][i]=0;
	
	for(int i=1; i<=m; i++)
		for(int j=1;j<=n;j++)
			if(A[i]==B[j])
			{
				D[i][j] = D[i-1][j-1] + 1;
				C[i][j] = 3;
			}
			else if(D[i-1][j] >= D[i][j-1])
			{
				D[i][j] = D[i-1][j];
				C[i][j] = 2;
			}
			else
			{
				D[i][j] = D[i][j-1];
				C[i][j] = 1;
			}
	Print(C,A,m,n);

}
