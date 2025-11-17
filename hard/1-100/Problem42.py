from typing import List


class Problem42:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0

        left = 0
        right = len(height) - 1
        leftmax = height[left]
        rightmax = height[right]
        water = 0

        while left < right:
            if leftmax <= rightmax:
                left += 1
                leftmax = max(leftmax, height[left])
                water += leftmax - height[left]
            else:
                right -= 1
                rightmax = max(rightmax, height[right])
                water += rightmax - height[right]

        return water


if __name__ == "__main__":
    solution = Problem42()
    print(solution.trap([0,1,0,2,1,0,1,3,2,1,2,1]))  # 6
