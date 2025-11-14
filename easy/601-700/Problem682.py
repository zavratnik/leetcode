from typing import List


class Problem682:
    def calPoints(self, operations: List[str]) -> int:
        stack: List[int] = []
        ans = 0

        for opr in operations:
            if opr not in "+DC":  
                val = int(opr)
                stack.append(val)
                ans += val
            else:
                if opr == 'C':
                    last = stack.pop()
                    ans -= last

                elif opr == 'D':
                    last = stack[-1]
                    doubled = 2 * last
                    stack.append(doubled)
                    ans += doubled

                elif opr == '+':
                    s = stack[-1] + stack[-2]
                    stack.append(s)
                    ans += s

        return ans


if __name__ == "__main__":
    solution = Problem682()
    result = solution.calPoints(["5", "2", "C", "D", "+"])
    print(result)  # 30
