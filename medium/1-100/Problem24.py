from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Problem24:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head

        prev = dummy
        curr = head

        while curr and curr.next:
            nextN = curr.next         
            nextNextN = curr.next.next 

            nextN.next = curr
            curr.next = nextNextN
            prev.next = nextN

            prev = curr
            curr = nextNextN

        return dummy.next


def build_linked_list(values):
    dummy = ListNode()
    curr = dummy
    for v in values:
        curr.next = ListNode(v)
        curr = curr.next
    return dummy.next


def print_list(head):
    arr = []
    while head:
        arr.append(head.val)
        head = head.next
    print(arr)


if __name__ == "__main__":
    solution = Problem24()

    head = build_linked_list([1, 2, 3, 4])
    res = solution.swapPairs(head)
    print_list(res)  # [2, 1, 4, 3]

    head = build_linked_list([1])
    res = solution.swapPairs(head)
    print_list(res)  # [1]

    head = build_linked_list([])
    res = solution.swapPairs(head)
    print_list(res)  # []
