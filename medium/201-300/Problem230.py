from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Problem230:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        def dfs(node: Optional[TreeNode]) -> List[int]:
            if not node:
                return []

            left = dfs(node.left)
            right = dfs(node.right)

            return left + [node.val] + right

        sorted_vals = dfs(root)
        return sorted_vals[k - 1]


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
    solution = Problem230()

    root = build_tree_from_list([3, 1, 4, None, 2])
    print(solution.kthSmallest(root, 1))  # 1
    print(solution.kthSmallest(root, 2))  # 2
    print(solution.kthSmallest(root, 3))  # 3
