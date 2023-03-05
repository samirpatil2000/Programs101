class Solution {

    public int dfs(String word1, String word2, int i, int j, int[][] memo){
        if (i == word1.length() && j == word2.length()){
            return 0;
        }
        if (memo[i][j] != -1){
            return memo[i][j];
        }
        if (i == word1.length()){
            return word2.length() - j;
        }
        if (j == word2.length()){
            return word1.length() - i;
        }
        
        int result;
        if (word1.charAt(i) == word2.charAt(j)){
            result = dfs(word1, word2, i + 1, j + 1, memo);
        } else {
            result = Math.min(
                Math.min(
                    dfs(word1, word2, i + 1, j, memo),
                    dfs(word1, word2, i, j + 1, memo)
                ), dfs(word1, word2, i + 1, j + 1, memo)
            ) + 1;
        }
        memo[i][j] = result;
        return result;
    }

    public int minDistance(String word1, String word2){
        int m = word1.length();
        int n = word2.length();
        int[][] memo = new int[m][n];
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                memo[i][j] = -1;
            }
        }
        return dfs(word1, word2, 0, 0, memo);
    }

}


public class Main {
    public static void main(String[] args){
        String s1 = "intention";
        String s2 = "execution";
        Solution solution = new Solution();
        System.out.println(solution.minDistance(s1, s2));
    }
}