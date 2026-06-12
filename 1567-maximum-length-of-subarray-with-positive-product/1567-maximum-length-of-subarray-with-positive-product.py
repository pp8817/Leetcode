
# 양수 곱 조건
## 모두 양수
## 음수가 짝수개
## 단, 0이 포함되는 경우는 제외

# 시간복잡도 O(N): nums의 길이만큼 1번만 순회
# 공간복잡도 O(1): 5개의 변수만 사용
class Solution:
    def getMaxLen(self, nums: List[int]) -> int:
        positive_len = 0 # 양수곱 부분배열 길이
        negative_len = 0 # 음수곱 부분배열 길이
        answer = 0

        for num in nums:
            if num > 0: # 양수라면
                positive_len += 1
                
                if negative_len != 0: # 음수곱 부분배열이 존재한다면 +1
                    negative_len += 1
            elif num < 0:
                prev_positive_len = positive_len
                prev_negative_len = negative_len

                if prev_negative_len != 0:
                    positive_len = prev_negative_len + 1
                else:
                    positive_len = 0
                
                negative_len = prev_positive_len + 1
        
            else:
                positive_len = 0
                negative_len = 0

            answer = max(answer, positive_len)
    
        return answer