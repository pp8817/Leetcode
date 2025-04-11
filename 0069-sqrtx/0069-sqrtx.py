class Solution:
    def mySqrt(self, x: int) -> int:
        ans = 1
        if x == 0:
            return 0

        for i in range(2, x//2+1):
            if i**2 <= x:
                ans = i
            else:
                break
        
        return ans
