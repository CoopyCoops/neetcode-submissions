# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head
        count = 0
        while head:
           count += 1
           head = head.next

        target = count - n
        idx = 0
        prev = dummy
        head = dummy.next
        while head:
            if idx == target:
                prev.next = head.next
                break
            idx += 1
            head = head.next
            prev = prev.next
        
        return dummy.next

