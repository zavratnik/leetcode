class Problem1544:
    def makeGood(self, s: str) -> str:
        stack = []

        for ch in s:
            if not stack:
                stack.append(ch)
                continue

            # če sta enaki črki v različnih velikostih (razlika ASCII = 32)
            if abs(ord(ch) - ord(stack[-1])) == 32:
                stack.pop()
            else:
                stack.append(ch)

        return "".join(stack)


if __name__ == "__main__":
    solution = Problem1544()
    print(solution.makeGood("leEeetcode"))  # "leetcode"
    print(solution.makeGood("abBAcC"))     # ""
    print(solution.makeGood("s"))          # "s"
