import random
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Problem382:
    def __init__(self, head: Optional[ListNode]):
        self.nodes = []

        while head:
            self.nodes.append(head.val)
            head = head.next

    def getRandom(self) -> int:
        return random.choice(self.nodes)


if __name__ == "__main__":
    # build linked list: 1 -> 2 -> 3
    head = ListNode(1, ListNode(2, ListNode(3)))

    solution = Problem382(head)

    # call getRandom multiple times
    for _ in range(5):
        print(solution.getRandom())
