# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
#class MountainArray:
#    def get(self, index: int) -> int:
#    def length(self) -> int:

class Solution:
    def findInMountainArray(self, target: int, mountainArr: 'MountainArray') -> int:
        N = mountainArr.length()
        left, right = 0, N - 1

        # peak index 찾기
        while left < right:
            mid = (left + right) // 2
            
            if mountainArr.get(mid) < mountainArr.get(mid+1): # peak는 mid보다 오른쪽에 있다.
                left = mid + 1
            else: # peak는 mid보다 왼쪽에 있다
                right = mid
            
        peak = left

        # 오름차순 구간에서 target 찾기
        left, right = 0, peak

        while left <= right:
            mid = (left + right) // 2
            num = mountainArr.get(mid)

            if num == target:
                return mid
            elif num < target:
                left = mid + 1
            else:
                right = mid - 1
        
        # 내림차순 구간에서 target 찾기
        left, right = peak + 1, N - 1

        while left <= right:
            mid = (left + right) // 2
            num = mountainArr.get(mid)

            if num == target:
                return mid
            elif num < target:
                right = mid - 1
            else:
                left = mid + 1
        
        return -1
