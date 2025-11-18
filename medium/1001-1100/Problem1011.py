from typing import List


class Problem1011:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        left = max(weights)
        right = sum(weights)

        while left < right:
            middle = left + (right - left) // 2
            counter = 1
            weight = 0

            for w in weights:
                if weight + w > middle:
                    counter += 1
                    weight = w
                else:
                    weight += w

            if counter > days:
                left = middle + 1
            else:
                right = middle

        return left


if __name__ == "__main__":
    solution = Problem1011()
    print(solution.shipWithinDays([1,2,3,4,5,6,7,8,9,10], 5))  # 15
    print(solution.shipWithinDays([3,2,2,4,1,4], 3))           # 6
    print(solution.shipWithinDays([1,2,3,1,1], 4))             # 3
