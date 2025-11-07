from bisect import bisect_left, insort
from typing import List


class Problem315:
    def countSmaller(self, nums: List[int]) -> List[int]:
        ans = []
        sorted_seen = []

        for num in reversed(nums):
            pos = bisect_left(sorted_seen, num)
            ans.append(pos)
            insort(sorted_seen, num)

        return ans[::-1]


if __name__ == "__main__":
    solution = Problem315()

    nums = [5, 2, 6, 1]
    result = solution.countSmaller(nums)
    print(result)  # [2, 1, 1, 0]
