# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ans = ListNode()
        carry = 0
        while l1 and l2:
            num1 = l1.val
            num2 = l2.val
            tot = num1 + num2 + carry
            ones = tot % 10     
            ans.next = ListNode(ones)
            ans = ans.next
            if tot >= 10:
                carry = 1
            else:
                carry = 0
            l1 = l1.next
            l2 = l2.next
        
        while l1:
            num1 = l1.val
            tot = num1 + carry
            ones = tot % 10
            ans.next = ListNode(ones)
            ans = ans.next
            if tot >= 10:
                carry = 1
            else:
                carry = 0
            l1 = l1.next
        
        while l2:
            num2 = l2.val
            tot = num2 + carry
            ones = tot % 10
            ans.next = ListNode(ones)
            ans = ans.next
            if tot >= 10:
                carry = 1
            else:
                carry = 0
            l2 = l2.next

        if carry == 1 and not l1 and not l2:
            ans.next = ListNode(carry)
        
        return dummy.next


