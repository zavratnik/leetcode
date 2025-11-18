import math
from typing import List


class Problem875:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)

        while left < right:
            middle = left + (right - left) // 2
            counter = 0

            for p in piles:
                counter += math.ceil(p / middle)

            if counter > h:
                left = middle + 1
            else:
                right = middle

        return left


if __name__ == "__main__":
    solution = Problem875()
    print(solution.minEatingSpeed([3, 6, 7, 11], 8))       # 4
    print(solution.minEatingSpeed([30, 11, 23, 4, 20], 5)) # 30
    print(solution.minEatingSpeed([30, 11, 23, 4, 20], 6)) # 23
