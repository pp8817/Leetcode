# 시계는 360도이며, 항상 더 작은 각도를 반환한다.
# - 분침: 1분에 6도 이동
# - 시침: 1시간에 30도, 1분에 0.5도 이동
#
# 시간복잡도: O(1)
# 공간복잡도: O(1)
class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        FULL_ANGLE = 360
        HOUR_TO_DEGREE = 30
        MINUTE_TO_DEGREE = 6
        HOUR_MINUTE_TO_DEGREE = 0.5

        if hour == 12:
            hour = 0

        minute_angle = minutes * MINUTE_TO_DEGREE
        hour_angle = hour * HOUR_TO_DEGREE + minutes * HOUR_MINUTE_TO_DEGREE

        angle_diff = abs(minute_angle - hour_angle)

        return min(angle_diff, FULL_ANGLE - angle_diff)