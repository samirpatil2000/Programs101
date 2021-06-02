#include<iostream>
#include<vector>

using namespace std;

int maxAreaOfIsland(vector<vector<int>>& grid) {
    int count = 0;
    n = grid.size(), m = grid[0].size();
    for (int i = 0; i < n; i++) 
        for (int j = 0; j < m; j++)
            if (grid[i][j]) {
                ans = max(ans, dfs(i, j, grid));
            }
    return count;
}
int dfs(int row,int col,vector<vector<int>> &grid){
    if (row<0 || col<0 || row>=grid.size() || col>=grid[0].size() || grid[row][col]==0){
        return 0;
    }
    int dr[]={-1,+1,0,0};
    int dc[]={0,0,-1,+1};
    grid[row][col]=0;
    int count_=1;
    for (int i=0;i<4;i++){
        count_+=dfs(row+dr[i],col+dc[i],grid);
    }
    return count_;

}

int main(){
    maxAreaOfIsland();

}

class Solution {
public:
    // int maxAreaOfIsland(vector<vector<int>>& grid) {
    //     int ans = 0;
    //     n = grid.size(), m = grid[0].size();
    //     for (int i = 0; i < n; i++) 
    //         for (int j = 0; j < m; j++)
    //             if (grid[i][j]) ans = max(ans, trav(i, j, grid));
    //     return ans;
    // }
    int maxAreaOfIsland(vector<vector<int>>& grid) {
        int count = 0;
        int n = grid.size(), m = grid[0].size();
        for (int i = 0; i < n; i++) 
            for (int j = 0; j < m; j++)
                if (grid[i][j]) {
                    ans = max(ans, dfs(i, j, grid));
                }
        return count;
    }
private:
    // int n, m;
    // int trav(int i, int j, vector<vector<int>>& grid) {
    //     if (i < 0 || j < 0 || i >= n || j >= m || !grid[i][j]) return 0;
    //     grid[i][j] = 0;
    //     return 1 + trav(i-1, j, grid) + trav(i, j-1, grid) + trav(i+1, j, grid) + trav(i, j+1, grid);
    // }
    int dfs(int row,int col,vector<vector<int>> &grid){
        if (row<0 || col<0 || row>=grid.size() || col>=grid[0].size() || grid[row][col]==0){
            return 0;
        }
        int dr[]={-1,+1,0,0};
        int dc[]={0,0,-1,+1};
        grid[row][col]=0;
        int count_=1;
        for (int i=0;i<4;i++){
            count_+=dfs(row+dr[i],col+dc[i],grid);
        }
        return count_;
    }
};

