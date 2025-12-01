class Problem224:
    def calculate(self, s: str) -> int:
        stack = []
        res = 0
        current_num = 0
        sign = 1

        for ch in s:
            if ch.isdigit():
                current_num = current_num * 10 + int(ch)

            elif ch == "+":
                res += current_num * sign
                current_num = 0
                sign = 1

            elif ch == "-":
                res += current_num * sign
                current_num = 0
                sign = -1

            elif ch == "(":
                stack.append(res)
                stack.append(sign)
                res = 0
                sign = 1

            elif ch == ")":
                res += current_num * sign
                current_num = 0

                outer_sign = stack.pop()
                outer_res = stack.pop()

                res = outer_res + outer_sign * res


        res += current_num * sign
        return res


if __name__ == "__main__":
    solution = Problem224()

    print(solution.calculate("1 + 1"))          # 2
    print(solution.calculate(" 2-1 + 2 "))      # 3
    print(solution.calculate("(1+(4+5+2)-3)+(6+8)"))  # 23
