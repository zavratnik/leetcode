from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Problem2:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        newList = dummy
        transfer = 0

        while l1 or l2 or transfer:
            total = transfer

            if l1:
                total += l1.val
                l1 = l1.next
            if l2:
                total += l2.val
                l2 = l2.next

            transfer = total // 10
            total = total % 10

            node = ListNode(total)
            newList.next = node
            newList = newList.next

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
    solution = Problem2()

    l1 = build_linked_list([2, 4, 3])
    l2 = build_linked_list([5, 6, 4])

    result = solution.addTwoNumbers(l1, l2)
    print_linked_list(result)   # [7, 0, 8]

    l1 = build_linked_list([0])
    l2 = build_linked_list([0])
    result = solution.addTwoNumbers(l1, l2)
    print_linked_list(result)   # [0]
