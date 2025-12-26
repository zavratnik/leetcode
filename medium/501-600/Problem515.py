from typing import Optional, List
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Problem515:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        q = deque([root])
        ans = []

        while q:
            current_max = q[0].val

            for _ in range(len(q)):
                node = q.popleft()
                if node.val > current_max:
                    current_max = node.val
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

            ans.append(current_max)

        return ans


if __name__ == "__main__":
    # build tree:
    #       1
    #      / \
    #     3   2
    #    / \   \
    #   5   3   9
    root = TreeNode(
        1,
        TreeNode(
            3,
            TreeNode(5),
            TreeNode(3)
        ),
        TreeNode(
            2,
            None,
            TreeNode(9)
        )
    )

    solution = Problem515()
    result = solution.largestValues(root)
    print(result)  # [1, 3, 9]
