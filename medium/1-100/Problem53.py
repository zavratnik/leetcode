from typing import List


class Problem53:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSum = float('-inf')
        currentSum = 0

        for num in nums:
            currentSum += num

            if currentSum > maxSum:
                maxSum = currentSum

            if currentSum < 0:
                currentSum = 0

        return maxSum


if __name__ == "__main__":
    solution = Problem53()

    print(solution.maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))  # 6
    print(solution.maxSubArray([1]))                             # 1
    print(solution.maxSubArray([5, 4, -1, 7, 8]))                # 23
