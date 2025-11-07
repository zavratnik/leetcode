from typing import List


class Problem739:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        ans = [0] * len(temperatures)

        for i in range(len(temperatures)):
            while stack and temperatures[i] > temperatures[stack[-1]]:
                j = stack.pop()
                ans[j] = i - j
            stack.append(i)

        return ans


if __name__ == "__main__":
    solution = Problem739()
    result = solution.dailyTemperatures([73, 74, 75, 71, 69, 72, 76, 73])
    print(result)  # [1, 1, 4, 2, 1, 1, 0, 0]
