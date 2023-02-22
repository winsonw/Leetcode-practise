# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.ma = -1001
        self.dive(root)
        return self.ma
    
    def dive(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        l = self.dive(root.left)
        r = self.dive(root.right)
        s = root.val + max(0,l) + max(0,r)
        if s > self.ma:
            self.ma = s
        root.val = root.val + max(0,l,r)
        return root.val