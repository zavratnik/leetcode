from typing import List


class Problem78:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        res: List[List[int]] = []
        temp: List[int] = []

        def backtrack(i: int):
            if i == n:
                res.append(temp[:])
                return

            backtrack(i + 1)

            temp.append(nums[i])
            backtrack(i + 1)
            temp.pop()

        backtrack(0)
        return res


if __name__ == "__main__":
    solution = Problem78()
    print(solution.subsets([1, 2, 3]))
    # [[], [3], [2], [2, 3], [1], [1, 3], [1, 2], [1, 2, 3]]
