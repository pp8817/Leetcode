# 모든 아이는 최소 1개의 사탕을 받아야 한다.
# 자신의 양옆 이웃보다 점수가 높은 아이는 더 많은 사탕을 받아야 한다.
# 최소 사탕 개수 반환

# 시간 복잡도: O(N)
# 공간 복잡도: O(N)
class Solution:
    def candy(self, ratings: List[int]) -> int:
        N = len(ratings) # 아이의 수
        candies = [1] * N # 모든 아이에게 사탕 1개씩 배분

        for i in range(1, N): # 왼쪽 비교
            if ratings[i] > ratings[i-1]:
                candies[i] = candies[i-1] + 1

        for i in range(N-2, -1, -1): # 오른쪽 비교
            if ratings[i] > ratings[i+1]:
                candies[i] = max(candies[i], candies[i+1] + 1) # 더 많은 사탕을 받은 경우를 고려해 max() 사용
        
        return sum(candies)