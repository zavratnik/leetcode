class Problem191:
    def hammingWeight(self, n: int) -> int:
        binary = bin(n)[2:]
        counter = 0

        for ch in binary:
            if ch == '1':
                counter += 1

        return counter


if __name__ == "__main__":
    solution = Problem191()

    n = 11  # binary 1011
    result = solution.hammingWeight(n)
    print(result)  # 3
