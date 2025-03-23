class Solution:
    def jump(self, nums: List[int]) -> int:
        temp = now = count = 0
        
        while now < len(nums)-1:
            max_ = 0
            for i in range(temp, now+1):
                max_ = max(max_, i+nums[i])
            temp = now+1
            now = max_
            count += 1
        return count
