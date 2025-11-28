import re
from typing import List


class Problem819:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        words = re.findall(r"[a-zA-Z]+", paragraph.lower())
        freq = {}

        for w in words:
            if w not in freq and w not in banned:
                freq[w] = 1
            elif w not in banned:
                freq[w] += 1

        res = max(freq, key=freq.get)
        return res


if __name__ == "__main__":
    solution = Problem819()

    paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
    banned = ["hit"]

    print(solution.mostCommonWord(paragraph, banned))  # "ball"
