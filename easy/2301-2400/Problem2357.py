from typing import List

class Problem2357:
    def minimumOperations(self, nums: List[int]) -> int:
        freq = {}

        for num in nums:
            if num != 0:
                freq[num] = freq.get(num, 0) + 1

        return len(freq)


if __name__ == "__main__":
    solution = Problem2357()
    print(solution.minimumOperations([1, 5, 0, 3, 5]))  # 3
    print(solution.minimumOperations([0]))              # 0
