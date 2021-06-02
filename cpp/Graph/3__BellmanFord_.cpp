#include<iostream>
#include<vector>



using namespace std;

struct node
{
    int u;
    int v;
    int wt;
    node(int first,int second,int weight){
        u=first;
        v=second;
        wt=weight;
    }
};


int main(){
    // n=6
    // edges=[[0,1,10],[0,2,1],[2,3,1],[1,3,1],[1,4,1],[4,5,10]]
    int N,m;
    cin>> N >> m;
    vector<node> edges;
    for (int i=0;i<m;i++){
        int u,v,wt;
        cin>> u >> v >> wt;
        edges.push_back(node(u,v,wt))
    }
    int src;
    cin>>src;
    int infinity=10000000;
    vector<int> dist(N,infinity);
    for (int i =0;i<=N-1;i++){
        for (auto it:edges){
            if (dist[it.u]+it.wt<dist[it.v]){
                dist[it.v]=dist[it.u]+it.wt;
            }
        }
    }
    int flag=0;
    for (auto it:edges){
        if (dist[it.u]+it.wt<dist[it.v]){
            cout<<"Negative Wt";
            flag=1;
            break;
        }
    }
}