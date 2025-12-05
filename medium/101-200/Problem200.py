from typing import List


class Problem200:
    def numIslands(self, grid: List[List[str]]) -> int:
        num_islands = 0
        rows, cols = len(grid), len(grid[0])

        def dfs(r: int, c: int):
            if (
                r < 0 or r >= rows or
                c < 0 or c >= cols or
                grid[r][c] == '0'
            ):
                return

            grid[r][c] = '0'  

            dfs(r - 1, c)
            dfs(r + 1, c)
            dfs(r, c - 1)
            dfs(r, c + 1)

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == '1':
                    num_islands += 1
                    dfs(i, j)

        return num_islands


if __name__ == "__main__":
    solution = Problem200()

    grid1 = [
        ["1","1","1","1","0"],
        ["1","1","0","1","0"],
        ["1","1","0","0","0"],
        ["0","0","0","0","0"]
    ]
    print(solution.numIslands(grid1))  # 1

    grid2 = [
        ["1","1","0","0","0"],
        ["1","1","0","0","0"],
        ["0","0","1","0","0"],
        ["0","0","0","1","1"]
    ]
    print(solution.numIslands(grid2))  # 3
