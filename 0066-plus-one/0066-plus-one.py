class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        s = int("".join(map(str, digits)))+1

        ans = []

        for i in str(s):
            ans.append(int(i))

        return ans