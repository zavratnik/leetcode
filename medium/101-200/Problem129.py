from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Problem129:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        def dfs(node: Optional[TreeNode], curr: int) -> int:
            if not node:
                return 0

            curr = curr * 10 + node.val

            if not node.left and not node.right:
                return curr

            left_sum = dfs(node.left, curr)
            right_sum = dfs(node.right, curr)

            return left_sum + right_sum

        return dfs(root, 0)


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
    solution = Problem129()

    root = build_tree_from_list([1, 2, 3])
    print(solution.sumNumbers(root))  # 25  (12 + 13)

    root = build_tree_from_list([4, 9, 0, 5, 1])
    print(solution.sumNumbers(root))  # 1026 (495 + 491 + 40)
