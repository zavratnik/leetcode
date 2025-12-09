from typing import List


class Problem77:
    def combine(self, n: int, k: int) -> List[List[int]]:
        temp: List[int] = []
        res: List[List[int]] = []

        def backtrack(i: int):
            if len(temp) == k:
                res.append(temp[:])
                return

            for j in range(i, n + 1):
                temp.append(j)
                backtrack(j + 1)
                temp.pop()

        backtrack(1)
        return res


if __name__ == "__main__":
    solution = Problem77()

    print(solution.combine(4, 2))
    # [
    #   [1, 2],
    #   [1, 3],
    #   [1, 4],
    #   [2, 3],
    #   [2, 4],
    #   [3, 4]
    # ]

    print(solution.combine(1, 1))
    # [[1]]
