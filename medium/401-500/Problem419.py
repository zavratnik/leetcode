from typing import List


class Problem419:
    def countBattleships(self, board: List[List[str]]) -> int:
        if not board:
            return 0

        rows, cols = len(board), len(board[0])
        numOfShips = 0

        for r in range(rows):
            for c in range(cols):
                if board[r][c] == '.':
                    continue

                if r > 0 and board[r - 1][c] == 'X':
                    continue

                if c > 0 and board[r][c - 1] == 'X':
                    continue

                numOfShips += 1

        return numOfShips


if __name__ == "__main__":
    solution = Problem419()

    board = [
        ["X", ".", ".", "X"],
        [".", ".", ".", "X"],
        [".", ".", ".", "X"]
    ]

    result = solution.countBattleships(board)
    print(result)  # 2
