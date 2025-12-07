from typing import List


class Problem289:
    def gameOfLife(self, board: List[List[int]]) -> None:
        rows, cols = len(board), len(board[0])

        def helper(r: int, c: int) -> int:
            neighbours = 0

            for i in range(r - 1, r + 2):
                for j in range(c - 1, c + 2):
                    if (
                        i < 0 or i >= rows or
                        j < 0 or j >= cols or
                        (i == r and j == c)
                    ):
                        continue

                    if board[i][j] in (1, 3):
                        neighbours += 1

            return neighbours

        for i in range(rows):
            for j in range(cols):
                nei = helper(i, j)

                if board[i][j] == 1:
                    if nei in (2, 3):
                        board[i][j] = 3
                else:
                    if nei == 3:
                        board[i][j] = 2

        for i in range(rows):
            for j in range(cols):
                if board[i][j] == 1:
                    board[i][j] = 0
                elif board[i][j] in (2, 3):
                    board[i][j] = 1


if __name__ == "__main__":
    game = Problem289()

    board = [
        [0, 1, 0],
        [0, 0, 1],
        [1, 1, 1],
        [0, 0, 0]
    ]

    game.gameOfLife(board)
    print(board)
    # Pričakovano:
    # [
    #   [0, 0, 0],
    #   [1, 0, 1],
    #   [0, 1, 1],
    #   [0, 1, 0]
    # ]
