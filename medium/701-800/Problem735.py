from typing import List


class Problem735:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []

        for ast in asteroids:
            if ast >= 0:
                stack.append(ast)
                continue

            while stack and 0 <= stack[-1] < abs(ast):
                stack.pop()
            if not stack or stack[-1] < 0:
                stack.append(ast)
            elif stack and abs(ast) == stack[-1]:
                stack.pop()

        return stack


if __name__ == "__main__":
    solution = Problem735()
    print(solution.asteroidCollision([5, 10, -5]))       # [5, 10]
    print(solution.asteroidCollision([8, -8]))           # []
    print(solution.asteroidCollision([10, 2, -5]))       # [10]
    print(solution.asteroidCollision([-2, -1, 1, 2]))    # [-2, -1, 1, 2]