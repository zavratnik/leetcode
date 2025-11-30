from typing import List


class Problem40:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        n = len(candidates)
        candidates.sort()
        res: List[List[int]] = []
        temp: List[int] = []

        def backtrack(i: int, current_sum: int):
            if current_sum == target:
                res.append(temp[:])
                return

            if i == n or current_sum > target:
                return

            next_index = i + 1
            while next_index < n and candidates[next_index] == candidates[i]:
                next_index += 1

            backtrack(next_index, current_sum)

            temp.append(candidates[i])
            backtrack(i + 1, current_sum + candidates[i])
            temp.pop()

        backtrack(0, 0)
        return res


if __name__ == "__main__":
    solution = Problem40()

    print(solution.combinationSum2([10, 1, 2, 7, 6, 1, 5], 8))
    # [[1,1,6], [1,2,5], [1,7], [2,6]]

    print(solution.combinationSum2([2, 5, 2, 1, 2], 5))
    # [[1,2,2], [5]]
