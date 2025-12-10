from typing import Optional
from collections import deque


class Node:
    def __init__(self, val: int = 0, left: 'Optional[Node]' = None,
                 right: 'Optional[Node]' = None, next: 'Optional[Node]' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Problem116:
    def connect(self, root: Optional[Node]) -> Optional[Node]:
        if not root:
            return root

        q = deque()
        q.append(root)

        while q:
            current_level = len(q)
            prev = None

            for _ in range(current_level):
                node = q.popleft()

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

                if prev is not None:
                    prev.next = node
                prev = node

            prev.next = None

        return root


if __name__ == "__main__":
    # Minimalen test primer
    root = Node(1,
                Node(2, Node(4), Node(5)),
                Node(3, Node(6), Node(7)))

    sol = Problem116()
    connected = sol.connect(root)

    # Preverimo povezave na prvi dveh nivojih
    print(connected.left.val, "->", connected.left.next.val)           # 2 -> 3
    print(connected.left.left.val, "->", connected.left.left.next.val) # 4 -> 5
