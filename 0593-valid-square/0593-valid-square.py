# -10^4 <= xi, yi <= 10^4

# 모든 경우의 수의 선 길이를 구한다.
## 정의1)정사각형: 각 변(4)개의 길이가 같다.
## + 정의2) 두 대각선의 길이가 같다. (마름모의 경우 1번 케이스에서 정사각형으로 판단 됨)
## + 모든 점이 [0,0]인 경우 -> 정의 1,2를 만족하지만 정사각형이 아님

class Solution:
    def validSquare(self, p1: List[int], p2: List[int], p3: List[int], p4: List[int]) -> bool:
        points = [p1, p2, p3, p4]

        distances = []
        for i in range(4):
            for j in range(i+1, 4):
                point_1, point_2 = points[i], points[j]
                dist = (point_1[0] - point_2[0]) ** 2 + (point_1[1] - point_2[1]) ** 2
                distances.append(dist)

        distances.sort() # 오름차순으로 정렬
        
        return (
            distances[0] == distances[3] and # 각 변의 길이가 모두 같다.
            distances[4] == distances[5] and # 두 대각선의 길이가 같다.
            distances[0] > 0 # 모든 변의 길이가 0보다 크다.
        )