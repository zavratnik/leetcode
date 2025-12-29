import random
from typing import List


class Problem528:
    def __init__(self, w: List[int]):
        self.prefix = []
        self.total = 0

        for weight in w:
            self.total += weight
            self.prefix.append(self.total)

    def pickIndex(self) -> int:
        random_index = random.randint(1, self.total)

        left, right = 0, len(self.prefix)

        while left < right:
            mid = left + (right - left) // 2

            if self.prefix[mid] < random_index:
                left = mid + 1
            else:
                right = mid

        return left


if __name__ == "__main__":
    weights = [1, 3, 2]
    solution = Problem528(weights)

    # pick index multiple times to see distribution
    results = [solution.pickIndex() for _ in range(10)]
    print(results)
