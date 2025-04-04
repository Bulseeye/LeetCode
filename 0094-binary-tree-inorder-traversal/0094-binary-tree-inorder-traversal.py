# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # need to create new func or else res keeps getting resetted
        res = []
        def dfs(root):
            if not root:
                return None

            dfs(root.left)
            res.append(root.val)
            dfs(root.right)
        dfs(root)
        return res
    