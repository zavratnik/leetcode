from collections import deque


class Problem225:
    def __init__(self):
        self.q = deque()

    def push(self, x: int) -> None:
        self.q.append(x)
        n = len(self.q)

        for _ in range(n - 1):
            self.q.append(self.q.popleft())

    def pop(self) -> int:
        return self.q.popleft()

    def top(self) -> int:
        return self.q[0]

    def empty(self) -> bool:
        return len(self.q) == 0


if __name__ == "__main__":
    stack = Problem225()

    stack.push(1)
    stack.push(2)
    print(stack.top())    # 2
    print(stack.pop())    # 2
    print(stack.empty()) # False
