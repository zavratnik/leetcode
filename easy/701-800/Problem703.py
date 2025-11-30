import heapq
from typing import List


class Problem703:
    def __init__(self, k: int, nums: List[int]):
        self.k_highest = k
        self.scores = nums
        heapq.heapify(self.scores)

        while len(self.scores) > k:
            heapq.heappop(self.scores)

    def add(self, val: int) -> int:
        heapq.heappush(self.scores, val)

        if len(self.scores) > self.k_highest:
            heapq.heappop(self.scores)

        return self.scores[0]


if __name__ == "__main__":
    kthLargest = Problem703(3, [4, 5, 8, 2])

    print(kthLargest.add(3))   # 4
    print(kthLargest.add(5))   # 5
    print(kthLargest.add(10))  # 5
    print(kthLargest.add(9))   # 8
    print(kthLargest.add(4))   # 8
