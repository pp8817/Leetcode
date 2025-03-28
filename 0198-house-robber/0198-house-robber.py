class Solution:
    def rob(self, nums: List[int]) -> int:
        N = len(nums)
        nums = [0] + nums
        dp = [0]*(N+1)
        dp[1] = nums[1]
        for i in range(2, N+1):
            dp[i] = max(dp[i-1], dp[i-2]+nums[i])

        return dp[N]