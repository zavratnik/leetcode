from typing import List


class Problem55:
    def canJump(self, nums: List[int]) -> bool:
        bestIndex = 0

        for i, num in enumerate(nums):
            if i > bestIndex:
                return False
            bestIndex = max(bestIndex, i + num)

        return True


if __name__ == "__main__":
    solution = Problem55()

    print(solution.canJump([2, 3, 1, 1, 4]))   # True
    print(solution.canJump([3, 2, 1, 0, 4]))   # False
    print(solution.canJump([0]))              # True
