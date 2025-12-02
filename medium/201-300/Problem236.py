from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Problem236:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        def dfs(node: Optional[TreeNode]):
            if not node:
                return None

            if node == p or node == q:
                return node

            left = dfs(node.left)
            right = dfs(node.right)

            if left and right:
                return node
            elif left:
                return left
            elif right:
                return right
            else:
                return None

        return dfs(root)


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


def find_node(root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
    if not root:
        return None
    if root.val == val:
        return root

    left = find_node(root.left, val)
    if left:
        return left
    return find_node(root.right, val)


if __name__ == "__main__":
    solution = Problem236()

    root = build_tree_from_list([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4])

    p = find_node(root, 5)
    q = find_node(root, 1)

    lca = solution.lowestCommonAncestor(root, p, q)
    print(lca.val)  # 3

    p = find_node(root, 5)
    q = find_node(root, 4)

    lca = solution.lowestCommonAncestor(root, p, q)
    print(lca.val)  # 5
