class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def dfs(node, currentSum):
            if not node:
                return False

            currentSum += node.val

            if not node.left and not node.right:
                return currentSum == targetSum
            
            return dfs(node.right, currentSum) or dfs(node.left, currentSum)

        return dfs(root, 0)