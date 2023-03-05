class Solution {
    productExceptSelf(nums, n){
      //code here
      var arr_1 = Array(n).fill(1);
      var arr_2 = Array(n).fill(1);
      
      for(var i = 1; i < nums.length; i ++){
        arr_1[i] = nums[i - 1] * arr_1[i - 1];
        var lastIndex = n - i - 1;
        arr_2[lastIndex] = arr_2[lastIndex + 1] * nums[lastIndex + 1]
        
      }
      var result = [];
      for(var i = 0; i < nums.length; i ++){
          result[i] = arr_1[i] * arr_2[i]
      }
      return result
    }
}