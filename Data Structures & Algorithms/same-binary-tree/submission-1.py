# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        isSame = True

        def dfs(p,q):
            nonlocal isSame
            if not p and not q:
                return
            elif not p and q:
                isSame = False
            elif not q and p:
                isSame = False
            
            try:
                dfs(p.left,q.left)
                dfs(p.right,q.right)
                if p.val != q.val:
                    isSame = False
            except AttributeError:
                isSame = False

            return 
        
        dfs(p,q)
        return isSame
        