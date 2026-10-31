# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        idxes = {values: index for index, values in enumerate(inorder)}
        self.preidx = 0
        def dfs(l,r):
            if l > r:
                return
            
            val = preorder[self.preidx]
            root = TreeNode(val)
            self.preidx += 1
            mid = idxes[val]
            root.left = dfs(l,mid-1)
            root.right = dfs(mid+1,r)
            return root
        root = dfs(0,len(preorder)-1)
        return root