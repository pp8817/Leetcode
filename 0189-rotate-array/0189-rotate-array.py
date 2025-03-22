class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        n = len(nums)
        k %= n

        # 배열의 전부를 뒤집고
        reverse(nums, 0, n-1)
        # 앞쪽 k개를 다시 뒤집고
        reverse(nums, 0, k-1)
        # 나머지를 뒤집으면 완성
        reverse(nums, k, n-1)

def reverse(nums, start, end):
    while start < end:
        nums[start], nums[end] = nums[end], nums[start]
        start += 1
        end -= 1