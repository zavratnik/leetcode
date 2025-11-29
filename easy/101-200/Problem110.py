from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Problem110:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs_height(node: Optional[TreeNode]) -> int:
            if not node:
                return 0

            left_height = dfs_height(node.left)
            right_height = dfs_height(node.right)

            if left_height == -1 or right_height == -1:
                return -1

            if abs(left_height - right_height) > 1:
                return -1

            return 1 + max(left_height, right_height)

        return dfs_height(root) != -1


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
    solution = Problem110()

    root1 = build_tree_from_list([3, 9, 20, None, None, 15, 7])
    print(solution.isBalanced(root1))  # True

    root2 = build_tree_from_list([1, 2, 2, 3, 3, None, None, 4, 4])
    print(solution.isBalanced(root2))  # False
