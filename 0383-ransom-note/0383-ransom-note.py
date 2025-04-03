from collections import Counter

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        maps = {}
        for ch in magazine:
            if ch in maps:
                maps[ch] += 1
            else:
                maps[ch] = 1

        for r in ransomNote:
            if r not in maps or maps[r] == 0:
                return False
            else:
                maps[r] -= 1
        return True