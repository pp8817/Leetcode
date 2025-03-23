class Solution:
    def jump(self, nums: List[int]) -> int:
        N = len(nums)
        dp = [int(1e9)]*N # 각 인덱스까지 점프 횟수
        dp[0]=0
        for i in range(N):
            for j in range(1, nums[i]+1):
                if i+j<N:
                    dp[i+j] = min(dp[i+j], dp[i]+1)
        return dp[N-1]
