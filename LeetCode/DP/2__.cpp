#include<iostream>
#include<vector>
using namespace std;

class Solution {
public:
    int maxResult(vector<int>& nums, int k) {
        vector<int> dp(0,nums.size());
        dp[0]=nums[0];
        for(int i=0,i<n;i++){
            int max_=-2**32;
            for (int j=i-1;max(i-k-1,-1);j--){
                max_=max(dp[j]+nums[i],max_);
            }
            dp[i]=max_;
        }
        return dp[nums.size()-1];
    }
};
int main(){
    Solution sol;
    vector<int> nums;
    nums={10,-5,-2,4,0,3};
    int k = 3;
    cout<<sol.maxResult(nums,k)<<endl;
}