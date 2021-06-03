#include<iostream>
#include<vector>

using namespace std;




class Solution {
public:
    bool isInterleave(string s1, string s2, string s3) {
        int k,i,j=0;
        if (s3.size()!=s1.size()+s2.size()){
            return false;
        }
        while (k<s3.size() && i<s1.size() && j<s2.size()){
            if (s1[i]==s3[k]){
                i++;k++;
            }else if(s2[j]==s3[k]){
                j++;k++;
            }else{
                return false;
            }
        }
        return true;
    }    
};

int main(){
    Solution sol;
    string s1 = "aabcc", s2 = "dbbca", s3 = "aadbbbaccc";
    
    cout<<"The solution is "<< sol.isInterleave(s1,s2,s3) <<endl;
}
