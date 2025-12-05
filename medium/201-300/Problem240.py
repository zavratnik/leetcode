from typing import List


class Problem240:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        r, c = 0, len(matrix[0]) - 1

        while r < len(matrix) and c >= 0:
            candidate = matrix[r][c]

            if candidate > target:
                c -= 1
            elif candidate < target:
                r += 1
            else:
                return True

        return False


if __name__ == "__main__":
    solution = Problem240()

    matrix = [
        [1,  4,  7, 11, 15],
        [2,  5,  8, 12, 19],
        [3,  6,  9, 16, 22],
        [10,13, 14,17, 24],
        [18,21, 23,26, 30]
    ]

    print(solution.searchMatrix(matrix, 5))    # True
    print(solution.searchMatrix(matrix, 20))   # False
