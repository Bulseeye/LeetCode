# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # the final array
        res = []
        # create a deque to traverse
        q = collections.deque()
        # add first tree element in the q
        q.append(root)

        # run until q is empty
        while q:
            # for every level run the length
            qlen = len(q)
            # create an new array for every level
            level = []

            for _ in range(qlen):
                # pop the most left from the queue and catch it in tNode
                tNode = q.popleft()
                if tNode:
                    #append the values to the level
                    level.append(tNode.val)
                    #append the left and right node value 
                    #from the popped node.
                    q.append(tNode.left)
                    q.append(tNode.right)
            # add the created [] to the res [] == [[]]
            if level:
                res.append(level)
        # if the queue is empty retun the res
        return res
                