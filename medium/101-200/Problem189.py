from typing import List


class Problem189:
    def rotate(self, nums: List[int], k: int) -> None:
        n = len(nums)
        k = k % n

        if k != 0:
            nums[k:], nums[:k] = nums[:-k], nums[-k:]


if __name__ == "__main__":
    solution = Problem189()

    nums = [1, 2, 3, 4, 5, 6, 7]
    solution.rotate(nums, 3)
    print(nums)  # [5, 6, 7, 1, 2, 3, 4]

    nums = [-1, -100, 3, 99]
    solution.rotate(nums, 2)
    print(nums)  # [3, 99, -1, -100]
