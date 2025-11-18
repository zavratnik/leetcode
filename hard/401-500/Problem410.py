from typing import List


class Problem410:
    def splitArray(self, nums: List[int], k: int) -> int:
        left = max(nums)
        right = sum(nums)

        while left < right:
            middle = left + (right - left) // 2
            counter = 1
            max_sum = 0

            for num in nums:
                if max_sum + num > middle:
                    counter += 1
                    max_sum = num
                else:
                    max_sum += num

            if counter > k:
                left = middle + 1
            else:
                right = middle

        return left


if __name__ == "__main__":
    solution = Problem410()
    print(solution.splitArray([7, 2, 5, 10, 8], 2))  # 18
    print(solution.splitArray([1, 2, 3, 4, 5], 2))   # 9
    print(solution.splitArray([1, 4, 4], 3))         # 4
