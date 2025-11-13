from typing import List
import operator as op


class Problem150:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operand = {
            "+": op.add,
            "-": op.sub,
            "*": op.mul,
            "/": lambda a, b: int(a / b)  # trunc proti 0
        }

        for token in tokens:
            if token not in operand:
                stack.append(int(token))
            else:
                num1 = stack.pop()
                num2 = stack.pop()
                temp = operand[token](num2, num1)
                stack.append(temp)

        return stack[0]


if __name__ == "__main__":
    solution = Problem150()

    tokens = ["2", "1", "+", "3", "*"]
    result = solution.evalRPN(tokens)
    print(result)  # 9

    tokens2 = ["4", "13", "5", "/", "+"]
    result2 = solution.evalRPN(tokens2)
    print(result2)  # 6

    tokens3 = ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]
    result3 = solution.evalRPN(tokens3)
    print(result3)  # 22
