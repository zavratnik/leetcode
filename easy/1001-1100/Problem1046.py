import heapq
from typing import List


class Problem1046:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap: List[int] = []

        # zgradimo max-heap z negativnimi vrednostmi
        for s in stones:
            heapq.heappush(heap, -s)

        while len(heap) > 1:
            y = heapq.heappop(heap)
            x = heapq.heappop(heap)

            if x != y:
                y -= x
                heapq.heappush(heap, y)

        return abs(heap[0]) if heap else 0


if __name__ == "__main__":
    solution = Problem1046()

    print(solution.lastStoneWeight([2, 7, 4, 1, 8, 1]))  # 1
    print(solution.lastStoneWeight([1]))               # 1
