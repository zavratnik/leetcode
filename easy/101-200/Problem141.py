from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Problem141:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        fast = head
        slow = head

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

            if slow == fast:
                return True

        return False


def build_linked_list(values, pos: int):
    if not values:
        return None

    nodes = [ListNode(v) for v in values]

    for i in range(len(nodes) - 1):
        nodes[i].next = nodes[i + 1]

    if pos != -1:
        nodes[-1].next = nodes[pos]

    return nodes[0]


if __name__ == "__main__":
    solution = Problem141()

    head1 = build_linked_list([3, 2, 0, -4], 1)
    print(solution.hasCycle(head1))  # True

    head2 = build_linked_list([1, 2], -1)
    print(solution.hasCycle(head2))  # False
