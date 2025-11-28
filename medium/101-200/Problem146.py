class ListNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None


class Problem146:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.node_map = {}

        self.head = ListNode(-1, -1)
        self.tail = ListNode(-1, -1)

        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        if key not in self.node_map:
            return -1

        node = self.node_map[key]

        self._remove(node)
        self._add(node)

        return node.value

    def put(self, key: int, value: int) -> None:
        if key in self.node_map:
            old_node = self.node_map[key]
            self._remove(old_node)

        node = ListNode(key, value)
        self.node_map[key] = node
        self._add(node)

        if len(self.node_map) > self.capacity:
            node_to_delete = self.head.next
            self._remove(node_to_delete)
            del self.node_map[node_to_delete.key]

    def _add(self, node):
        prev_end = self.tail.prev
        prev_end.next = node

        node.prev = prev_end
        node.next = self.tail

        self.tail.prev = node

    def _remove(self, node):
        prevN = node.prev
        nextN = node.next
        prevN.next = nextN
        nextN.prev = prevN


if __name__ == "__main__":
    lru = Problem146(2)

    lru.put(1, 1)
    lru.put(2, 2)
    print(lru.get(1))   # 1

    lru.put(3, 3)       # evicts key 2
    print(lru.get(2))   # -1

    lru.put(4, 4)       # evicts key 1
    print(lru.get(1))   # -1
    print(lru.get(3))   # 3
    print(lru.get(4))   # 4
