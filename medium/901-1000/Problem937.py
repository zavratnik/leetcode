from typing import List


class Problem937:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        ans: List[str] = []

        digits: List[str] = []
        words: List[tuple] = []

        for log in logs:
            identifier = log.split()[0]
            content = " ".join(log.split()[1:])

            if content[0].isdigit():
                digits.append(log)
            else:
                words.append((content, identifier))

        words.sort(key=lambda x: (x[0], x[1]))

        for content, identifier in words:
            ans.append(identifier + " " + content)

        ans.extend(digits)

        return ans


if __name__ == "__main__":
    solution = Problem937()
    logs = ["dig1 8 1 5 1", "let1 art can", "dig2 3 6",
            "let2 own kit dig", "let3 art zero"]

    print(solution.reorderLogFiles(logs))
    # ['let1 art can', 'let3 art zero', 'let2 own kit dig', 'dig1 8 1 5 1', 'dig2 3 6']
