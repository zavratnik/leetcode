class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        n = len(candidates)
        candidates.sort()
        res = []
        temp = []

        def backtrack(i, current_sum):
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