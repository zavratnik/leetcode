from typing import Optional
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Problem513:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        q = deque()
        q.append(root)

        leftMost = root.val

        while q:
            current_level = len(q)
            leftMost = q[0].val  

            for _ in range(current_level):
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

        return leftMost


if __name__ == "__main__":
    # build tree:
    #       1
    #      / \
    #     2   3
    #        / \
    #       4   5
    root = TreeNode(
        1,
        TreeNode(2),
        TreeNode(
            3,
            TreeNode(4),
            TreeNode(5)
        )
    )

    solution = Problem513()
    result = solution.findBottomLeftValue(root)
    print(result)  # 4
