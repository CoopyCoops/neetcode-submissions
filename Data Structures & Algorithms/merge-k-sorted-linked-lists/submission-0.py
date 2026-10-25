# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None

        while len(lists) > 1:
            # merge two lists
            list1 = lists.pop(0)
            list2 = lists.pop(0)
            dummy = prev = ListNode()

            while list1 and list2:
                if list1.val < list2.val:
                    prev.next = list1
                    list1 = list1.next
                else:
                    prev.next = list2
                    list2 = list2.next
                prev = prev.next
            
            if list1:
                prev.next = list1
            else:
                prev.next = list2
            
            merged_list = dummy.next
            lists.append(merged_list)

        return lists[0]

        