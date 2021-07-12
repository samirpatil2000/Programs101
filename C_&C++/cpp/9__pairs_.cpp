#include<iostream>
#include<vector>

using namespace std;


bool comparator(pair<int,int> p1,pair<int,int>p2){
    return p1.first<p2.first;
}

int main(){
    // pair<int ,char> p;
    // p.first=3;
    // p.second='f';
    // return 0;

    vector<pair<int,int> > v;
    int arr[]={10,16,7,14,5,3,2,9};
    for (int i=0; i<sizeof(arr)/sizeof(arr[0]);i++){
        v.push_back(make_pair(arr[i],i));
    }
    sort(v.begin(),v.end(),comparator);
    for (int i=0;i<v.size();i++){
        // cout<<v[i].first<<" , "<<v[i].second<<endl;
        arr[v[i].second]=i;
    }

    for (int i=0;i<v.size();i++){
        cout<<arr[i]<<endl;
        // arr[v[i].second]=i;
    }
     
}