class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        N = len(triangle)
        dp = [[0]*i for i in range(1, N+1)]
        dp[0][0] = triangle[0][0]

        for i in range(1, N):
            dp[i][0] = triangle[i][0] + dp[i-1][0]  # 왼쪽 끝
            dp[i][i] = triangle[i][i] + dp[i-1][i-1]  # 오른쪽 끝
            for j in range(1, i):  # 중간
                dp[i][j] = triangle[i][j] + min(dp[i-1][j-1], dp[i-1][j])

        return min(dp[-1])