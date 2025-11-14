from typing import List


class Problem496:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        ng = {}
        ans: List[int] = []

        for num in nums2:
            while stack and num > stack[-1]:
                ng[stack[-1]] = num
                stack.pop()
            stack.append(num)

        while stack:
            ng[stack.pop()] = -1

        for num in nums1:
            ans.append(ng.get(num))

        return ans


if __name__ == "__main__":
    solution = Problem496()
    result = solution.nextGreaterElement([4, 1, 2], [1, 3, 4, 2])
    print(result)  # [-1, 3, -1]
