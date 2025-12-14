from bisect import bisect_left
from typing import List


class Problem300:
    def lengthOfLIS(self, nums: List[int]) -> int:
        sequence = []

        for n in nums:
            if not sequence or sequence[-1] < n:
                sequence.append(n)
            else:
                idx = bisect_left(sequence, n)
                sequence[idx] = n

        return len(sequence)


if __name__ == "__main__":
    solution = Problem300()

    nums = [10, 9, 2, 5, 3, 7, 101, 18]
    result = solution.lengthOfLIS(nums)
    print(result)  # 4
