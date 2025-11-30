from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Problem1448:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(node: Optional[TreeNode], maxVal: int) -> int:
            if not node:
                return 0

            res = 1 if node.val >= maxVal else 0
            maxVal = max(maxVal, node.val)

            if node.left:
                res += dfs(node.left, maxVal)
            if node.right:
                res += dfs(node.right, maxVal)

            return res

        return dfs(root, root.val)


def build_tree_from_list(values):
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
    solution = Problem1448()

    root = build_tree_from_list([3, 1, 4, 3, None, 1, 5])
    print(solution.goodNodes(root))  # 4
