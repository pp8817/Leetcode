class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pair = {")": "(", "}":"{","]":"["}

        for ch in s:
            if ch in "({[":
                stack.append(ch)
            elif stack and stack[-1] == pair[ch]:
                stack.pop()
            else:
                return False

        return not stack