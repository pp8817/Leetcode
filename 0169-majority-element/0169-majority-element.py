class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort(reverse=False)
        n = len(nums)
        return nums[n//2]