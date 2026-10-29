# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        q = collections.deque()
        q.append(root)

        res = []

        while q:
            n = len(q)
            right = None
            for i in range(n):
                node = q.popleft()
                if node:
                    q.append(node.left)
                    q.append(node.right)
                    right = node
            if right:
                res.append(right.val)

        return res
        