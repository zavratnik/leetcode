from typing import List


class Problem153:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1

        while left < right:
            mid = left + (right - left) // 2

            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid

        return nums[left]


if __name__ == "__main__":
    solution = Problem153()
    print(solution.findMin([3,4,5,1,2]))     # 1
    print(solution.findMin([4,5,6,7,0,1,2])) # 0
    print(solution.findMin([11,13,15,17]))   # 11
