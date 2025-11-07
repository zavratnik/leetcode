from typing import List


class Problem155:
    def __init__(self):
        self.stack: List[int] = []
        self.minStack: List[int] = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.minStack:
            self.minStack.append(val)
        else:
            self.minStack.append(val if val < self.minStack[-1] else self.minStack[-1])

    def pop(self) -> None:
        self.stack.pop()
        self.minStack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minStack[-1]


if __name__ == "__main__":
    minStack = Problem155()

    minStack.push(-2)
    minStack.push(0)
    minStack.push(-3)
    print(minStack.getMin())  # -3
    minStack.pop()
    print(minStack.top())     # 0
    print(minStack.getMin())  # -2
