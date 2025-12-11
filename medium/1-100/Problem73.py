from typing import List


class Problem73:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        rows, cols = len(matrix), len(matrix[0])

        def turnZero(r: int, c: int):
            for i in range(rows):
                matrix[i][c] = 0
            for j in range(cols):
                matrix[r][j] = 0

        original_zeroes = []

        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == 0:
                    original_zeroes.append((i, j))

        for r, c in original_zeroes:
            turnZero(r, c)


if __name__ == "__main__":
    sol = Problem73()

    m = [
        [1, 1, 1],
        [1, 0, 1],
        [1, 1, 1]
    ]

    sol.setZeroes(m)
    print(m)
    # Pričakovano:
    # [
    #   [1, 0, 1],
    #   [0, 0, 0],
    #   [1, 0, 1]
    # ]
