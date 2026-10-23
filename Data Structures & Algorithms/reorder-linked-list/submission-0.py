# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        #find the mid-point of the linked list
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        #reverse the second-half of the linked list
        prev = None
        curr = slow.next
        slow.next = None
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp

        #merge the two linked lists together
        while head and prev:
            temp1 = head.next
            head.next = prev
            temp2 = prev.next
            prev.next = temp1
            head = temp1
            prev = temp2
            