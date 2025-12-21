from typing import List


class Problem406:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        ans = []

        people.sort(key=lambda x: (-x[0], x[1]))

        for p in people:
            ans.insert(p[1], p)

        return ans


if __name__ == "__main__":
    solution = Problem406()

    people = [[7, 0], [4, 4], [7, 1], [5, 0], [6, 1], [5, 2]]
    result = solution.reconstructQueue(people)

    print(result)
    # expected: [[5,0],[7,0],[5,2],[6,1],[4,4],[7,1]]
