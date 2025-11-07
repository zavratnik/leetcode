from typing import List


class Problem46:
    def permute(self, nums: List[int]) -> List[List[int]]:
        rezultat: List[List[int]] = []

        if len(nums) == 0:
            return []
        if len(nums) == 1:
            return [nums[:]]

        for i in range(len(nums)):
            prvi = nums[i]
            preostanek = nums[0:i] + nums[i + 1 :]

            for p in self.permute(preostanek):
                rezultat.append([prvi] + p)

        return rezultat


if __name__ == "__main__":
    solution = Problem46()

    nums = [1, 2, 3]
    result = solution.permute(nums)
    print(result)  # [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
