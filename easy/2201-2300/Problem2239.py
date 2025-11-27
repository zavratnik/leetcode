from typing import List


class Problem2239:
    def findClosestNumber(self, nums: List[int]) -> int:
        currentMin = nums[0]

        for num in nums:
            if abs(num) < abs(currentMin):
                currentMin = num
            elif abs(num) == abs(currentMin):
                currentMin = max(num, currentMin)

        return currentMin


if __name__ == "__main__":
    solution = Problem2239()
    print(solution.findClosestNumber([2, -1, 1]))   # 1
    print(solution.findClosestNumber([-4, -2, 2, 4])) # 2
    print(solution.findClosestNumber([1]))          # 1
