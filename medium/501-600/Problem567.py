class Problem567:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        freqs1 = {}

        for ch in s1:
            freqs1[ch] = freqs1.get(ch, 0) + 1

        n = len(s2)
        windowsize = len(s1)

        if n < windowsize:
            return False

        left = 0
        window = freqs1.copy()

        for right in range(n):
            if s2[right] not in window:
                window = freqs1.copy()
                left = right + 1
                continue

            window[s2[right]] -= 1

            while window[s2[right]] < 0:
                window[s2[left]] += 1
                left += 1

            if (right - left + 1) == windowsize:
                return True

        return False


if __name__ == "__main__":
    solution = Problem567()

    print(solution.checkInclusion("ab", "eidbaooo"))  # True
    print(solution.checkInclusion("ab", "eidboaoo"))  # False
    print(solution.checkInclusion("adc", "dcda"))     # True
