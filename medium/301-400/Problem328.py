from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Problem328:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        odd, even = head, head.next
        even_head = even

        while even and even.next:
            odd.next = even.next
            odd = odd.next

            even.next = odd.next
            even = even.next

        odd.next = even_head
        return head


if __name__ == "__main__":
    # build linked list: 1 -> 2 -> 3 -> 4 -> 5
    head = ListNode(1,ListNode(2,ListNode(3,ListNode(4,ListNode(5)))))

    solution = Problem328()
    result = solution.oddEvenList(head)

    # print result
    curr = result
    while curr:
        print(curr.val, end=" -> " if curr.next else "\n")
        curr = curr.next
