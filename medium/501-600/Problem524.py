from typing import List


class Problem524:
    def findLongestWord(self, s: str, dictionary: List[str]) -> str:
        def isSubsequence(word: str) -> bool:
            it = iter(s)
            for char in word:
                if char not in it:
                    return False
            return True

        dictionary.sort(key=lambda x: (-len(x), x))

        for word in dictionary:
            if isSubsequence(word):
                return word

        return ""


if __name__ == "__main__":
    solution = Problem524()

    s = "abpcplea"
    dictionary = ["ale", "apple", "monkey", "plea"]
    result = solution.findLongestWord(s, dictionary)
    print(result)  # apple
