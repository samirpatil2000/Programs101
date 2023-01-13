class Solution{

    findSubarray(arr){
        var result = 0;
        var currentSum = 0;
        const visited = {0: 1};
        for(var i = 0; i < arr.length; i++){
            currentSum += arr[i]
            if (visited[currentSum]){
                result += visited[currentSum]
            }else{
                visited[currentSum] = 0
            }
            visited[currentSum] ++;
        }
        return result;

    }
}
const sol = new Solution();
var arr = [0,0,5,5,0,0];
console.log(sol.findSubarray(arr, arr.length))