#include<iostream>
#include<vector>
using namespace std;


int main(){
    vector<int> v;
    v.push_back(2);
    v.push_back(1);

    for(int i=0;i<v.size();i++){
        cout<<v[i]<<endl;
    }

    vector<int>:: iterator it;
    for (it=v.begin();it!=v.end();it++){
        cout<<*it<<endl;
    }

    for (auto el:v){
        cout<<el<<endl;
    }

    vector<int> v2 (3,50);
    for (auto el:v2){
        cout<<el<<endl;
    }
    sort(v.begin(),v.end());
    for (auto el:v){
        cout<<el<<endl;
    }
}