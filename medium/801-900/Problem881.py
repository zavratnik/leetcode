from typing import List


class Problem881:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        if limit < max(people):
            return -1

        people.sort()

        left = 0
        right = len(people) - 1
        number_boats = 0

        while left <= right:
            if people[left] + people[right] > limit:
                number_boats += 1
                right -= 1
            else:
                number_boats += 1
                left += 1
                right -= 1

        return number_boats


if __name__ == "__main__":
    solution = Problem881()

    print(solution.numRescueBoats([1, 2], 3))          # 1
    print(solution.numRescueBoats([3, 2, 2, 1], 3))    # 3
    print(solution.numRescueBoats([3, 5, 3, 4], 5))    # -1
