from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Problem654:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        return self.buildBinaryTree(nums)

    def buildBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        if not nums:
            return None

        max_num = max(nums)
        max_num_index = nums.index(max_num)

        node = TreeNode(max_num)

        node.left = self.buildBinaryTree(nums[:max_num_index])
        node.right = self.buildBinaryTree(nums[max_num_index + 1:])

        return node


def preorder_traversal(root: Optional[TreeNode]) -> List[int]:
    if not root:
        return []
    return [root.val] + preorder_traversal(root.left) + preorder_traversal(root.right)


def inorder_traversal(root: Optional[TreeNode]) -> List[int]:
    if not root:
        return []
    return inorder_traversal(root.left) + [root.val] + inorder_traversal(root.right)


if __name__ == "__main__":
    solution = Problem654()

    nums = [3, 2, 1, 6, 0, 5]
    root = solution.constructMaximumBinaryTree(nums)

    print(preorder_traversal(root))  # [6, 3, 2, 1, 5, 0]
    print(inorder_traversal(root))   # [3, 2, 1, 6, 0, 5]
