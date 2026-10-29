"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        nodes = {None: None}
        dummy = temp = Node(-1)

        curr = head
        while curr:
            copy = Node(curr.val)
            nodes[curr] = copy
            curr = curr.next
        
        curr = head
        while curr:
            address = nodes[curr]
            address.next = nodes[curr.next]
            address.random = nodes[curr.random] 
            curr = curr.next
        
        return nodes[head]

