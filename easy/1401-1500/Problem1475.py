from typing import List


class Problem1475:
    def finalPrices(self, prices: List[int]) -> List[int]:
        stack: List[int] = []
        ans: List[int] = []

        for i in range(len(prices) - 1, -1, -1):
            while stack and stack[-1] > prices[i]:
                stack.pop()

            if stack:
                ans.append(prices[i] - stack[-1])
            else:
                ans.append(prices[i])

            stack.append(prices[i])

        return ans[::-1]


if __name__ == "__main__":
    solution = Problem1475()
    result = solution.finalPrices([8, 4, 6, 2, 3])
    print(result)  # [4, 2, 4, 2, 3]
