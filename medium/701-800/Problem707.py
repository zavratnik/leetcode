class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


class Problem707:
    def __init__(self):
        self.length = 0
        self.dummy = Node(0)

    def get(self, index: int) -> int:
        if self.length == 0 or index >= self.length or index < 0:
            return -1

        curr = self.dummy.next

        for _ in range(index):
            curr = curr.next

        return curr.val

    def addAtHead(self, val: int) -> None:
        new_node = Node(val)
        temp = self.dummy.next
        self.dummy.next = new_node
        new_node.next = temp

        self.length += 1

    def addAtTail(self, val: int) -> None:
        head = self.dummy
        new_node = Node(val)

        while head.next:
            head = head.next

        head.next = new_node
        self.length += 1

    def addAtIndex(self, index: int, val: int) -> None:
        if index < 0 or index > self.length:
            return
        if index == 0:
            self.addAtHead(val)
            return

        curr = self.dummy

        for _ in range(index):
            curr = curr.next

        new_node = Node(val)
        temp = curr.next
        curr.next = new_node
        new_node.next = temp

        self.length += 1

    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index >= self.length:
            return

        curr = self.dummy

        for _ in range(index):
            curr = curr.next

        to_delete = curr.next
        curr.next = to_delete.next

        self.length -= 1


if __name__ == "__main__":
    linkedList = Problem707()

    linkedList.addAtHead(1)
    linkedList.addAtTail(3)
    linkedList.addAtIndex(1, 2)    # 1 -> 2 -> 3
    print(linkedList.get(1))       # 2

    linkedList.deleteAtIndex(1)    # 1 -> 3
    print(linkedList.get(1))       # 3

    linkedList.deleteAtIndex(0)    # 3
    print(linkedList.get(0))       # 3
