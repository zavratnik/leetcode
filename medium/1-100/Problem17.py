from typing import List


class Problem17:
    def letterCombinations(self, digits: str) -> List[str]:
        phone_map = {
            "2": "abc", "3": "def", "4": "ghi", "5": "jkl",
            "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"
        }

        n = len(digits)
        if n == 0:
            return []

        temp = []
        ans: List[str] = []

        def backtrack(i: int):
            if i == n:
                ans.append("".join(temp))
                return

            for letter in phone_map[digits[i]]:
                temp.append(letter)
                backtrack(i + 1)
                temp.pop()

        backtrack(0)
        return ans


if __name__ == "__main__":
    solution = Problem17()

    print(solution.letterCombinations("23"))
    # ["ad","ae","af","bd","be","bf","cd","ce","cf"]

    print(solution.letterCombinations(""))
    # []

    print(solution.letterCombinations("2"))
    # ["a","b","c"]
