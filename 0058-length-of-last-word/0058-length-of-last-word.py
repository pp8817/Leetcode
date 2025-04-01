class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        li = list(s.split())
        return len(list(s.split())[-1])