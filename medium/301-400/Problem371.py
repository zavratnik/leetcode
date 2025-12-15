class Problem371:
    def getSum(self, a: int, b: int) -> int:
        MASK = 0xFFFFFFFF
        INT_MAX = 2**31 - 1

        while b != 0:
            carry = (a & b) & MASK
            a = (a ^ b) & MASK
            b = (carry << 1) & MASK

        return a if a <= INT_MAX else ~(a ^ MASK)


if __name__ == "__main__":
    solution = Problem371()

    a = 5
    b = -3
    result = solution.getSum(a, b)
    print(result)  # 2
