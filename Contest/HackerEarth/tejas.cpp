#include <bits/stdc++.h>

using namespace std;

int main(){
    vector<int> v = {6, 3, -1, -3, 4, -2, 2, 4, 6, -12, -7};

    unordered_map<int, list<int> > mp;
    int res = 0, s = 0;

    for(int i = 0; i < n; i++){
        s += arr[i];
        if(s == 0){
            res++;
            if(mp.find(s) != mp.end()){
                list<int> l = mp[s];
                for(auto it = l.begin(); it != l.end(); it++){
                    res++;
                }
                
                
            }
        }
            mp[s].push_back(i);
            
        
    }
    cout << res << endl;
}