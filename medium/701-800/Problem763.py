from typing import List


class Problem763:
    def partitionLabels(self, s: str) -> List[int]:
        last_index = {}
        ans: List[int] = []

        for i in range(len(s)):
            last_index[s[i]] = i

        start = 0
        end = 0

        for i, ch in enumerate(s):
            end = max(end, last_index[ch])

            if i == end:
                ans.append(end - start + 1)
                start = i + 1

        return ans


if __name__ == "__main__":
    solution = Problem763()

    print(solution.partitionLabels("ababcbacadefegdehijhklij"))
    # [9, 7, 8]

    print(solution.partitionLabels("eccbbbbdec"))
    # [10]
