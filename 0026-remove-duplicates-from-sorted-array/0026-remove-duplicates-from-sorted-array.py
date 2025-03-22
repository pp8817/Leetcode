class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0
        k = 1
        for i in range(1, len(nums)):
            if nums[i] != nums[i-1]: # 이전 요소와 값이 다르다면 유니크 값
                nums[k] = nums[i]
                k += 1 

        return k