from typing import List


class Problem45:
    def jump(self, nums: List[int]) -> int:
        num_jumps = 0
        near = 0
        far = 0

        while far < len(nums) - 1:
            furthest = 0

            for i in range(near, far + 1):
                furthest = max(furthest, i + nums[i])

            near = far + 1
            far = furthest
            num_jumps += 1

        return num_jumps


if __name__ == "__main__":
    solution = Problem45()

    print(solution.jump([2, 3, 1, 1, 4]))   # 2
    print(solution.jump([2, 3, 0, 1, 4]))   # 2
    print(solution.jump([1, 2, 1, 1, 1]))   # 3
