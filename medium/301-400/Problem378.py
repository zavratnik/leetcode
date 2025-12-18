from typing import List


class Problem378:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        rows, cols = len(matrix), len(matrix[0])
        element = rows * cols
        temp = []

        for i in range(element):
            r = i // cols
            c = i % cols
            temp.append(matrix[r][c])

        temp.sort()
        return temp[k - 1]


if __name__ == "__main__":
    solution = Problem378()

    matrix = [
        [1, 5, 9],
        [10, 11, 13],
        [12, 13, 15]
    ]
    k = 8

    result = solution.kthSmallest(matrix, k)
    print(result)  # 13
