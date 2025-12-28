from typing import List


class Problem522:
    def findLUSlength(self, strs: List[str]) -> int:
        def isSubsequence(s: str, t: str) -> bool:
            it = iter(t)
            for ch in s:
                if ch not in it:
                    return False
            return True

        strs.sort(key=lambda x: -len(x))

        for i, s in enumerate(strs):
            is_uncommon = True

            for j in range(len(strs)):
                if i != j and isSubsequence(s, strs[j]):
                    is_uncommon = False
                    break

            if is_uncommon:
                return len(s)

        return -1


if __name__ == "__main__":
    solution = Problem522()

    strs = ["aba", "cdc", "eae"]
    result = solution.findLUSlength(strs)
    print(result)  # 3
