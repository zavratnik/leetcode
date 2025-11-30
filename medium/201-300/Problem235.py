from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Problem235:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        curr = root

        while curr:
            if p.val > curr.val and q.val > curr.val:
                curr = curr.right
            elif p.val < curr.val and q.val < curr.val:
                curr = curr.left
            else:
                return curr


def build_bst_from_list(values):
    """
    Zgradi BST z zaporednim vstavljanjem vrednosti.
    """
    if not values:
        return None

    root = TreeNode(values[0])

    for val in values[1:]:
        curr = root
        while True:
            if val < curr.val:
                if curr.left:
                    curr = curr.left
                else:
                    curr.left = TreeNode(val)
                    break
            else:
                if curr.right:
                    curr = curr.right
                else:
                    curr.right = TreeNode(val)
                    break

    return root


def find_node(root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
    while root:
        if root.val == val:
            return root
        elif val < root.val:
            root = root.left
        else:
            root = root.right
    return None


if __name__ == "__main__":
    solution = Problem235()

    # BST: [6,2,8,0,4,7,9,3,5]
    root = build_bst_from_list([6, 2, 8, 0, 4, 7, 9, 3, 5])

    p = find_node(root, 2)
    q = find_node(root, 8)

    lca = solution.lowestCommonAncestor(root, p, q)
    print(lca.val)  # 6

    p = find_node(root, 2)
    q = find_node(root, 4)

    lca = solution.lowestCommonAncestor(root, p, q)
    print(lca.val)  # 2
