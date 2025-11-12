from typing import List


class Problem704:
    def search(self, nums: List[int], target: int) -> int:
        if target in nums:
            return nums.index(target)
        else:
            return -1


if __name__ == "__main__":
    solution = Problem704()

    nums = [4,5,6,7,0,1,2]
    target = 0
    result = solution.search(nums, target)
    print(result)  # 4
