from typing import Optional, List
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Problem199:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        q = deque()
        q.append(root)

        arr: List[int] = []

        while q:
            level_size = len(q)

            for i in range(level_size):
                node = q.popleft()

                # zadnji element v vsakem levelu je viden z desne
                if i == level_size - 1:
                    arr.append(node.val)

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

        return arr


def build_tree_from_list(values):
    """
    Gradi binarno drevo iz array predstavitve (level-order).
    None pomeni, da vozlišče ne obstaja.
    """
    if not values:
        return None

    nodes = [None if v is None else TreeNode(v) for v in values]
    kids = nodes[::-1]
    root = kids.pop()

    for node in nodes:
        if node:
            if kids:
                node.left = kids.pop()
            if kids:
                node.right = kids.pop()

    return root


if __name__ == "__main__":
    solution = Problem199()

    root = build_tree_from_list([1, 2, 3, None, 5, None, 4])
    print(solution.rightSideView(root))  # [1, 3, 4]
