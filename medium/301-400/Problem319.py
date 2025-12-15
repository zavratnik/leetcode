import math


class Problem319:
    def bulbSwitch(self, n: int) -> int:
        return int(math.sqrt(n))


if __name__ == "__main__":
    solution = Problem319()

    n = 25
    result = solution.bulbSwitch(n)
    print(result)  # 5
