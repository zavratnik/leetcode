from typing import List


class Problem119:
    def getRow(self, rowIndex: int) -> List[int]:
        ans: List[int] = [1]
        prev = 1

        for i in range(1, rowIndex + 1):
            next_val = prev * (rowIndex - i + 1) // i
            ans.append(next_val)
            prev = next_val

        return ans


if __name__ == "__main__":
    solution = Problem119()

    rowIndex = 3
    result = solution.getRow(rowIndex)
    print(result)  # [1, 3, 3, 1]
