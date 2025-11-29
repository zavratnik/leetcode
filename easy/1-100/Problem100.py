from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Problem100:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p is None and q is None:
            return True

        elif p is None or q is None:
            return False

        elif p.val != q.val:
            return False

        left = self.isSameTree(p.left, q.left)
        right = self.isSameTree(p.right, q.right)

        return True if left and right else False


def build_tree_from_list(values):
    """
    Zgradi binarno drevo iz level-order predstavitve.
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
    solution = Problem100()

    tree1 = build_tree_from_list([1, 2, 3])
    tree2 = build_tree_from_list([1, 2, 3])
    print(solution.isSameTree(tree1, tree2))  # True

    tree3 = build_tree_from_list([1, 2])
    tree4 = build_tree_from_list([1, None, 2])
    print(solution.isSameTree(tree3, tree4))  # False
