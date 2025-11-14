from typing import List


class Problem853:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []
        cars = list(zip(position, speed))

        cars.sort(key=lambda x: x[0], reverse=True)

        for pos, speed in cars:
            time = (target - pos) / speed

            if not stack:
                stack.append(time)
            else:
                last = stack[-1]
                if time <= last:
                    continue
                else:
                    stack.append(time)

        return len(stack)


if __name__ == "__main__":
    solution = Problem853()

    target = 12
    position = [10, 8, 0, 5, 3]
    speed = [2, 4, 1, 1, 3]
    result = solution.carFleet(target, position, speed)

    print(result)  # 3
