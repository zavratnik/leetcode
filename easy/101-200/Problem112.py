from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Problem112:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def dfs(node, curr_sum):
            if not node:
                return False

            if not node.left and not node.right:
                return curr_sum == node.val

            new_sum = curr_sum - node.val
            return dfs(node.left, new_sum) or dfs(node.right, new_sum)

        return dfs(root, targetSum)


if __name__ == "__main__":
    # build tree:
    #       5
    #      / \
    #     4   8
    #    /   / \
    #   11  13  4
    #  /  \
    # 7    2
    root = TreeNode(5,TreeNode(4,TreeNode(11,TreeNode(7),TreeNode(2)),),TreeNode(8,TreeNode(13),TreeNode(4,None,TreeNode(1))))

    solution = Problem112()
    result = solution.hasPathSum(root, 22)
    print(result)  # True
