//2014004948_이승재_508호

#include <stdio.h>
#include <stdlib.h>
#include <queue>
#include <string.h>
using namespace std;

priority_queue <pair <long long int, int> >q;

typedef struct node
{
	int weight;
	int index;
	bool checknum;
	node *next;
}node;

int main(void)
{
	int i,j, N;
	scanf("%d",&N);
	
	node* Node;
	Node = (node*)calloc(1,sizeof(node)*(N+1));
	
	node* tmp;

//	Node[1].weight = 0;
	Node[1].index = 1;
//	Node[1].checknum = 0;
	for(i=2; i<=N; i++)
	{	
		Node[i].weight = 99999;
		Node[i].index = i;
		//Node[i].checknum = 0;
	}
	
	int start, end, weight, count;
//	for(i=1; i<=N; i++)
//	{
//		scanf("%d %d",&start,&count);

	while(scanf("%d %d",&start,&count) != EOF)
	{
		for(j=1;j<=count;j++)
		{
			scanf("%d %d",&end,&weight);
			tmp = &Node[start];
			while(tmp->next)
				tmp=tmp->next;
			tmp->next = (node*)calloc(1,sizeof(node));
			tmp->next->index = end;
			tmp->next->weight = weight;
		}
	}
	
	// adjacent list complete

	q.push(make_pair(0,1));

	while(!q.empty())
	{
		int a = q.top().second;
		int aw = -(q.top().first);
		q.pop();
	
		tmp = Node[a].next;
		while(tmp)
		{
			int next = tmp->index;
			int nextw = tmp->weight+aw;
			if((Node[next].weight) > nextw)
			{
				Node[next].weight = nextw;
				q.push(make_pair(-nextw,next));
			}
			tmp = tmp->next;
			
		}

		// one index done.
	}		
	
	int max=0;
	for(i=2;i<=N;i++)
		if(max<Node[i].weight)
			max = Node[i].weight;
	
	printf("%d\n",max);
	
	for(i=1;i<=N;i++)
	{
		tmp = Node[i].next;
		while(tmp)
		{
			node* tmp2 = tmp;
			tmp=tmp->next;
			free(tmp2);
		}
	}
	free(Node);

	return 0;
}
