from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Problem98:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(node: Optional[TreeNode], minimum: float, maximum: float) -> bool:
            if not node:
                return True

            if not (minimum < node.val < maximum):
                return False

            left = dfs(node.left, minimum, node.val)
            right = dfs(node.right, node.val, maximum)

            return left and right

        return dfs(root, float("-inf"), float("inf"))


def build_tree_from_list(values: List[Optional[int]]):
    """
    Gradi binarno drevo iz level-order predstavitve.
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
    solution = Problem98()

    root1 = build_tree_from_list([2, 1, 3])
    print(solution.isValidBST(root1))  # True

    root2 = build_tree_from_list([5, 1, 4, None, None, 3, 6])
    print(solution.isValidBST(root2))  # False
