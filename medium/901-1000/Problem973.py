import heapq
import math
from typing import List


class Problem973:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap: List[List[float, List[int]]] = []

        for x, y in points:
            distance = math.sqrt(x * x + y * y)

            if len(heap) < k:
                heapq.heappush(heap, [-distance, [x, y]])
            else:
                if distance < -heap[0][0]:
                    heapq.heappop(heap)
                    heapq.heappush(heap, [-distance, [x, y]])

        res: List[List[int]] = []

        for _, point in heap:
            res.append(point)

        return res


if __name__ == "__main__":
    solution = Problem973()

    points = [[1, 3], [-2, 2], [5, 8], [0, 1]]
    k = 2
    print(solution.kClosest(points, k))  
    # primer izhoda: [[-2, 2], [0, 1]]
