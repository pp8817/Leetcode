class Solution:
    def canJump(self, nums: List[int]) -> bool:
        max_reach = 0
        for i, jump in enumerate(nums):
            if i > max_reach:
                return False # 현재 위치에 도달하지 못하면 종료
            max_reach = max(max_reach, i+jump)
        return True