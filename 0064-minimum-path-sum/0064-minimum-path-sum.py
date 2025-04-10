class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        dp = [[int(1e9) for _ in range(m)] for _ in range(n)]
        dp[0][0] = grid[0][0]

        d = [[1,0], [0,1]]
        
        for i in range(n):
            for j in range(m):
                for dx, dy in d:
                    rx, ry = i+dx, j+dy

                    if 0<=rx<n and 0<=ry<m:
                        dp[rx][ry] = min(dp[rx][ry], dp[i][j]+grid[rx][ry])

        return dp[n-1][m-1]