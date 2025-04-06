# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # recursive solution is just a inorder traversal
        # arr = []

        # def inorder(root):
        #     if not root:
        #         return

        #     inorder(root.left)
        #     arr.append(root.val)
        #     inorder(root.right)
        # inorder(root)
        # return arr[k-1]

        # Iterative
        stack = []
        cur = root

        # as long as we have a cur or a stack keep running the code.
        while cur or stack:
            while cur:
                stack.append(cur)
                cur = cur.left
            cur = stack.pop()

            k -= 1
            if k == 0:
                return cur.val
            cur = cur.right
          