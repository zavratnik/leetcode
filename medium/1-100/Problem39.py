from typing import List


class Problem39:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        n = len(candidates)
        res: List[List[int]] = []
        temp: List[int] = []

        def backtrack(i: int, current_sum: int):
            if current_sum == target:
                res.append(temp[:])
                return

            if current_sum > target or i == n:
                return

            temp.append(candidates[i])
            backtrack(i, current_sum + candidates[i])
            temp.pop()

            backtrack(i + 1, current_sum)

        backtrack(0, 0)
        return res


if __name__ == "__main__":
    solution = Problem39()
    print(solution.combinationSum([2, 3, 6, 7], 7))  
    # [[2, 2, 3], [7]]

    print(solution.combinationSum([2, 3, 5], 8))
    # [[2, 2, 2, 2], [2, 3, 3], [3, 5]]
