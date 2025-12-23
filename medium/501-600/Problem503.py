from typing import List


class Problem503:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n = len(nums)
        stack = []        
        ans = [-1] * n

        for i in range(2 * n):
            current_num = nums[i % n]

            while stack and current_num > nums[stack[-1]]:
                index = stack.pop()
                ans[index] = current_num

            if i < n:
                stack.append(i)

        return ans


if __name__ == "__main__":
    solution = Problem503()

    nums = [1, 2, 1]
    result = solution.nextGreaterElements(nums)
    print(result)  # [2, -1, 2]
