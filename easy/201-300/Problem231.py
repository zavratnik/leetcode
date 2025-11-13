class Problem231:
    def isPowerOfTwo(self, n: int) -> bool:
        return n > 0 and not (n & (n - 1))


if __name__ == "__main__":
    solution = Problem231()

    print(solution.isPowerOfTwo(1))   # True  (2^0)
    print(solution.isPowerOfTwo(16))  # True  (2^4)
    print(solution.isPowerOfTwo(3))   # False
    print(solution.isPowerOfTwo(0))   # False
