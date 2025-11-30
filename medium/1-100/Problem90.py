from typing import List


class Problem90:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        nums.sort()
        res: List[List[int]] = []
        temp: List[int] = []

        def backtrack(i: int):
            if i == n:
                res.append(temp[:])
                return

            next_index = i + 1
            while next_index < n and nums[next_index] == nums[i]:
                next_index += 1

            backtrack(next_index)

            temp.append(nums[i])
            backtrack(i + 1)
            temp.pop()

        backtrack(0)
        return res


if __name__ == "__main__":
    solution = Problem90()

    print(solution.subsetsWithDup([1, 2, 2]))
    # [[], [2], [2,2], [1], [1,2], [1,2,2]]

    print(solution.subsetsWithDup([0]))
    # [[], [0]]
