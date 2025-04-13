# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        
        def dfs(node, cursum):
            # check if we have a node if not return False
            if not node:
                return False

            cursum += node.val

            # calculate cursum and check if target = cursum
            if not node.left and not node.right:
                return targetSum == cursum


            # check if left or right return true else False
            if dfs(node.left, cursum) or dfs(node.right, cursum):
                return True
            else:
                return False
            
        # return the dfs
        return dfs(root, 0)