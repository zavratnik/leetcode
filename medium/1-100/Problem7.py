class Problem7:
    def reverse(self, x: int) -> int:
        temp_str = list(str(x))

        left = 1 if x < 0 else 0
        right = len(temp_str) - 1

        while left < right:
            temp = temp_str[left]
            temp_str[left] = temp_str[right]
            temp_str[right] = temp
            left += 1
            right -= 1

        reversed_str = ''.join(temp_str)
        reversed_int = int(reversed_str)

        if reversed_int < -2**31 or reversed_int > 2**31 - 1:
            return 0

        return reversed_int


if __name__ == "__main__":
    solution = Problem7()

    print(solution.reverse(123))      # 321
    print(solution.reverse(-123))     # -321
    print(solution.reverse(120))      # 21
    print(solution.reverse(0))        # 0
