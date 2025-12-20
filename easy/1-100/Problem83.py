from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Problem83:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head

        while curr and curr.next:
            nextN = curr.next
            if curr.val == nextN.val:
                curr.next = nextN.next
            else:
                curr = curr.next

        return head


if __name__ == "__main__":
    # build linked list: 1 -> 1 -> 2 -> 3 -> 3
    head = ListNode(1,ListNode(1,ListNode(2,ListNode(3,ListNode(3)))))

    solution = Problem83()
    result = solution.deleteDuplicates(head)

    # print result
    curr = result
    while curr:
        print(curr.val, end=" -> " if curr.next else "\n")
        curr = curr.next
