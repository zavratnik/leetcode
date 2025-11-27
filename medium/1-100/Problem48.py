from typing import List


class Problem48:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)

        for i in range(n):
            for j in range(i + 1, n):
                temp = matrix[i][j]
                matrix[i][j] = matrix[j][i]
                matrix[j][i] = temp

        for i in range(n):
            left = 0
            right = n - 1
            while left < right:
                temp = matrix[i][left]
                matrix[i][left] = matrix[i][right]
                matrix[i][right] = temp
                left += 1
                right -= 1


if __name__ == "__main__":
    solution = Problem48()

    matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]

    solution.rotate(matrix)
    print(matrix)
    # [
    #   [7, 4, 1],
    #   [8, 5, 2],
    #   [9, 6, 3]
    # ]
