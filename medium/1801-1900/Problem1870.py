import math
from typing import List


class Problem1870:
    def minSpeedOnTime(self, dist: List[int], hour: float) -> int:
        left = 1
        right = 10 ** 7

        if hour < len(dist) - 1:
            return -1

        while left < right:
            middle = left + (right - left) // 2
            counter = 0

            for i, d in enumerate(dist):
                if i == len(dist) - 1:
                    counter += d / middle      
                else:
                    counter += math.ceil(d / middle)

            if counter > hour:
                left = middle + 1
            else:
                right = middle

        return left


if __name__ == "__main__":
    solution = Problem1870()
    print(solution.minSpeedOnTime([1, 3, 2], 6))       # 1
    print(solution.minSpeedOnTime([1, 3, 2], 2.7))     # 3
    print(solution.minSpeedOnTime([1, 3, 2], 1.9))     # -1
