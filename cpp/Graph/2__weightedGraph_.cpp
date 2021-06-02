#include<iostream>
#include<vector>



using namespace std;

struct node
{
    int u;
    int v;
    int wt;
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
}