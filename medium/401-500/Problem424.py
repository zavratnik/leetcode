class Problem424:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        longest = 0
        n = len(s)
        freq = {}
        maxFreq = 0

        for right in range(n):
            freq[s[right]] = freq.get(s[right], 0) + 1
            maxFreq = max(maxFreq, freq[s[right]])

            changes = (right - left + 1) - maxFreq

            while changes > k:
                freq[s[left]] -= 1
                left += 1
                changes = (right - left + 1) - maxFreq

            longest = max(longest, right - left + 1)

        return longest


if __name__ == "__main__":
    solution = Problem424()

    print(solution.characterReplacement("ABAB", 2))      # 4
    print(solution.characterReplacement("AABABBA", 1))   # 4
