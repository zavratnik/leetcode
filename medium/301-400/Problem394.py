class Problem394:
    def decodeString(self, s: str) -> str:
        stack = []

        for ch in s:
            if ch != "]":
                stack.append(ch)
            else:
                temp = []

                while stack and stack[-1] != "[":
                    temp.append(stack.pop())

                stack.pop()  

                temp.reverse()
                temp = "".join(temp)

                num_string = ""
                while stack and stack[-1].isdigit():
                    num_string += stack.pop()

                num = int(num_string[::-1])

                temp *= num
                stack.append(temp)

        return "".join(stack)


if __name__ == "__main__":
    solution = Problem394()

    print(solution.decodeString("3[a]2[bc]"))       # "aaabcbc"
    print(solution.decodeString("3[a2[c]]"))        # "accaccacc"
    print(solution.decodeString("2[abc]3[cd]ef"))   # "abcabccdcdcdef"
