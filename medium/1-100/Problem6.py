class Problem6:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or numRows >= len(s):
            return s

        rows = [""] * numRows
        down = False
        currentRow = 0

        for ch in s:
            rows[currentRow] += ch

            if currentRow == 0 or currentRow == numRows - 1:
                down = not down

            currentRow += 1 if down else -1

        return "".join(rows)


if __name__ == "__main__":
    solution = Problem6()
    s = "PAYPALISHIRING"
    numRows = 3
    result = solution.convert(s, numRows)
    print(result)  # "PAHNAPLSIIGYIR"
