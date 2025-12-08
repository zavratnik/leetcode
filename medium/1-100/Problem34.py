from typing import List


class Problem34:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def first(nums: List[int], target: int) -> int:
            left, right = 0, len(nums) - 1
            ans = -1

            while left <= right:
                mid = left + (right - left) // 2

                if nums[mid] >= target:
                    if nums[mid] == target:
                        ans = mid
                    right = mid - 1
                else:
                    left = mid + 1

            return ans

        def last(nums: List[int], target: int) -> int:
            left, right = 0, len(nums) - 1
            ans = -1

            while left <= right:
                mid = left + (right - left) // 2

                if nums[mid] <= target:
                    if nums[mid] == target:
                        ans = mid
                    left = mid + 1
                else:
                    right = mid - 1

            return ans

        return [first(nums, target), last(nums, target)]


if __name__ == "__main__":
    solution = Problem34()

    print(solution.searchRange([5, 7, 7, 8, 8, 10], 8))    # [3, 4]
    print(solution.searchRange([5, 7, 7, 8, 8, 10], 6))    # [-1, -1]
    print(solution.searchRange([], 0))                    # [-1, -1]
