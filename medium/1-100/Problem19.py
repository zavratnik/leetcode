from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Problem19:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode()
        curr = dummy
        curr.next = head

        for _ in range(n):
            head = head.next

        while head:
            head = head.next
            curr = curr.next

        curr.next = curr.next.next

        return dummy.next


def build_linked_list(values):
    dummy = ListNode()
    curr = dummy
    for v in values:
        curr.next = ListNode(v)
        curr = curr.next
    return dummy.next


def print_linked_list(head):
    result = []
    while head:
        result.append(head.val)
        head = head.next
    print(result)


if __name__ == "__main__":
    solution = Problem19()

    head = build_linked_list([1, 2, 3, 4, 5])
    new_head = solution.removeNthFromEnd(head, 2)
    print_linked_list(new_head)   # [1, 2, 3, 5]

    head = build_linked_list([1])
    new_head = solution.removeNthFromEnd(head, 1)
    print_linked_list(new_head)   # []
