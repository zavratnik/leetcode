class Problem1209:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = []
        res = ""

        for ch in s:
            if not stack or ch != stack[-1][0]:
                stack.append((ch, 1))
            else:
                prev_char, count = stack.pop()
                new_count = count + 1

                if new_count == k:
                    continue
                else:
                    stack.append((prev_char, new_count))

        for char, count in stack:
            res += char * count

        return res


if __name__ == "__main__":
    solution = Problem1209()

    print(solution.removeDuplicates("abcd", 2))        # "abcd"
    print(solution.removeDuplicates("deeedbbcccbdaa", 3))  # "aa"
    print(solution.removeDuplicates("pbbcggttciiippooaais", 2))  # "ps"
