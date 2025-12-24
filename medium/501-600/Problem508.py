from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Problem508:
    def findFrequentTreeSum(self, root: Optional[TreeNode]) -> List[int]:
        freq = {}

        def dfs(node):
            if not node:
                return 0

            left_sum = dfs(node.left)
            right_sum = dfs(node.right)

            tree_sum = node.val + left_sum + right_sum
            freq[tree_sum] = freq.get(tree_sum, 0) + 1

            return tree_sum

        if not root:
            return []

        dfs(root)

        max_freq = max(freq.values())
        ans = []

        for s, c in freq.items():
            if c == max_freq:
                ans.append(s)

        return ans


if __name__ == "__main__":
    # build tree:
    #      5
    #     / \
    #    2  -3
    root = TreeNode(
        5,
        TreeNode(2),
        TreeNode(-3)
    )

    solution = Problem508()
    result = solution.findFrequentTreeSum(root)
    print(result)  # [2, -3, 4]
