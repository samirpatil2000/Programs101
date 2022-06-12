#include <bits/stdc++.h>
using namespace std;

vector<int>bfsgraph(int v,vector<int>adj[])
{
      vector<bool>vis(v,false);
      vector<int>bfs(v);
      for(int i=0;i<v;i++)				//taking the first node i=1 of a given graph
      {
      	if(vis[i]==false)					//if it is not visited then only go further
      	{
      		queue<int>q;			// take a queue q to push the element that is not visited
      		q.push(i);
      		vis[i]=true;			//make element visited
      		while(!q.empty())			//while queue is not empty traverse
      		{
      			int node=q.front();	//why q.front? -> bcause we want the first element we push(adj node) in the q not the top most 
      			q.pop();
      			bfs.push_back(node);    //storing answer here
				for(auto it : adj[node])
				{
					if(!vis[it])
					{
						q.push(it);
						vis[it]=true;
					}
				}
			}
		}
	}
	return bfs;
}

void print_ans(vector<int>&ans)
{
	 for(int i=0;i<ans.size();i++)
      {
      	cout << ans[i] <<" ";
	}
}

int main()
{
	int v;
	int e;
	cin >> v >> e;
	vector<int>adj[v+1];
	for(int i=0;i<e;i++)			// accepting for each vertex its corresponding edges
	{
		int u;
		int v;
		cin >> u >> v;
		adj[u].push_back(v);
		adj[v].push_back(u);
	}
      vector<int>ans=bfsgraph(v,adj);
      print_ans(ans);
     
	return 0;
}