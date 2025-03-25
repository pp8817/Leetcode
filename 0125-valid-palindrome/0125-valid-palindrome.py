class Solution:
    def is_alphanumberic(self, c):
        return ('a'<=c<='z') or ("A"<=c<="Z") or ("0"<=c<="9")
    def isPalindrome(self, s: str) -> bool:
        left, right = 0, len(s) - 1

        while left < right:
            while left < right and not self.is_alphanumberic(s[left]):
                left += 1
            while left < right and not self.is_alphanumberic(s[right]):
                right -= 1
            
            if s[left].lower() != s[right].lower():
                return False
            
            left += 1
            right -= 1
        
        return True

        