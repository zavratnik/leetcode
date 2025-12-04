import heapq
from typing import List
from collections import Counter


class Problem692:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        seen = Counter(words)

        heap = []
        for w, c in seen.items():
            heap.append((-c, w))   

        heapq.heapify(heap)

        ans: List[str] = []
        for _ in range(k):
            ans.append(heapq.heappop(heap)[1])

        return ans


if __name__ == "__main__":
    solution = Problem692()

    print(solution.topKFrequent(
        ["i", "love", "leetcode", "i", "love", "coding"], 2
    ))  
    # ["i", "love"]

    print(solution.topKFrequent(
        ["the", "day", "is", "sunny", "the", "the", "the", 
         "sunny", "is", "is"], 4
    ))
    # ["the", "is", "sunny", "day"]
