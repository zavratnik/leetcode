from typing import List


class Problem22:
    def generateParenthesis(self, n: int) -> List[str]:
        ans: List[str] = []
        temp: List[str] = []

        def backtrack(open_cnt: int, close_cnt: int):
            if open_cnt == n and close_cnt == n:
                ans.append("".join(temp[:]))
                return

            if open_cnt < n:
                temp.append("(")
                backtrack(open_cnt + 1, close_cnt)
                temp.pop()

            if close_cnt < open_cnt:
                temp.append(")")
                backtrack(open_cnt, close_cnt + 1)
                temp.pop()

        backtrack(0, 0)
        return ans


if __name__ == "__main__":
    solution = Problem22()

    print(solution.generateParenthesis(3))
    # ["((()))","(()())","(())()","()(())","()()()"]

    print(solution.generateParenthesis(1))
    # ["()"]
