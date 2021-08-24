#include <stdio.h>
#include <stdlib.h>

typedef struct 
{
	int start;
	int end;
} edge;

void ccr(edge *edges, int n, int *components, int N, int vertex, int component)
{
	int i;
	components[vertex] = component;
	for(i=0; i<=n; i++)
		if(edges[i].start == vertex || edges[i].end == vertex)
		{
			int neighbor = (edges[i].start == vertex) ? edges[i].end : edges[i].start;
			if(components[neighbor] == -1)
				ccr(edges, n, components, N, neighbor, component);
		}
}

int connected_components(edge *edges, int n, int N, int **components)
{
	int i;
	int component = 0;
	
//	*components = (int *)malloc(sizeof(int)*(N+1));
	for(i=0; i<=N; i++)
		(*components)[i] = -1;
	
	for(i=0; i<=N; i++)
		if((*components)[i] == -1)
		{
			ccr(edges,n,*components,N,i,component);
			component++;
		}

	return component;
}

int main(void)
{
	int *components;
	
	int N; 
	scanf("%d",&N);		//number of vertices
	
	components = (int *)malloc(sizeof(int)*(N+1));

	int v1,v2, i=0;
	edge *edges;
	edges = (edge*)malloc(sizeof(edge)*1000);

	while(scanf("%d %d", &v1,&v2) != EOF)
	{
		edges[i].start = v1;
		edges[i].end = v2;
		i++;
	}
	//i = # of edge
	int c = connected_components(edges,i,N,&components);
	printf("%d\n",c-1);

	for(i=1;i<=N;i++)
		printf("%d\n",(components)[i]);	
	
//	free(edges);
//	free(components);

	return 0;
	
}
