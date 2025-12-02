from typing import List


class Problem79:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])
        path = set()

        def dfs(r: int, c: int, i: int) -> bool:
            if i == len(word):
                return True

            if (r < 0 or r >= rows or
                c < 0 or c >= cols or
                word[i] != board[r][c] or
                (r, c) in path):
                return False

            path.add((r, c))

            res = (
                dfs(r + 1, c, i + 1) or
                dfs(r - 1, c, i + 1) or
                dfs(r, c + 1, i + 1) or
                dfs(r, c - 1, i + 1)
            )

            path.remove((r, c))
            return res

        for r in range(rows):
            for c in range(cols):
                if dfs(r, c, 0):
                    return True

        return False


if __name__ == "__main__":
    solution = Problem79()

    board = [
        ["A", "B", "C", "E"],
        ["S", "F", "C", "S"],
        ["A", "D", "E", "E"]
    ]

    print(solution.exist(board, "ABCCED"))  # True
    print(solution.exist(board, "SEE"))     # True
    print(solution.exist(board, "ABCB"))    # False
