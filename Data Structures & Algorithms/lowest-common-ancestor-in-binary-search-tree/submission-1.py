# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        curr = root.val
        if p.val > q.val:
            p,q = q,p

        if p.val == curr or q.val == curr:
            return root
        if p.val < curr and q.val > curr:
            return root
        
        if p.val < curr and q.val < curr:
            ans = self.lowestCommonAncestor(root.left, p, q)
        elif p.val > curr and q.val > curr:
            ans = self.lowestCommonAncestor(root.right, p, q)
        
        return ans