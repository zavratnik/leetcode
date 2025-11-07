class Problem58:
    def lengthOfLastWord(self, s: str) -> int:
        counter = 0

        for c in s[::-1]:
            if c == ' ' and counter == 0:
                continue
            elif c != ' ':
                counter += 1
            else:
                break

        return counter


if __name__ == "__main__":
    solution = Problem58()

    s = "Hello World"
    result = solution.lengthOfLastWord(s)
    print(result)  # 5
