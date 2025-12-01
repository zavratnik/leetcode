from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Problem113:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        result_paths: List[List[int]] = []

        def dfs(node: Optional[TreeNode], curr_sum: int, arr: List[int]):
            if not node:
                return

            arr.append(node.val)
            curr_sum += node.val

            if not node.left and not node.right and curr_sum == targetSum:
                result_paths.append(arr[:])

            dfs(node.left, curr_sum, arr)
            dfs(node.right, curr_sum, arr)

            arr.pop()

        dfs(root, 0, [])
        return result_paths


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
    solution = Problem113()

    root = build_tree_from_list([5, 4, 8, 11, None, 13, 4, 7, 2, None, None, 5, 1])
    print(solution.pathSum(root, 22))
    # [[5, 4, 11, 2], [5, 8, 4, 5]]
