# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists) == 0:
            return None
        return self.devideTo2List(lists, 0, len(lists) - 1)
    
    def devideTo2List(self, lists, l, r) -> Optional[ListNode]:
        if l > r:
            return None
        if l == r:
            return lists[l]
        
        mid = (l + r) // 2
        left = self.devideTo2List(lists, l, mid)
        right = self.devideTo2List(lists, mid + 1, r)
        return self.merge2Lists(left, right) 

    def merge2Lists(self, list1, list2) -> Optional[ListNode]: 
        dummy = ListNode(0)
        curr = dummy
        while list1 and list2:
            if list1.val <= list2.val:
                curr.next = list1
                list1 = list1.next
            else:
                curr.next = list2
                list2 = list2.next
            curr = curr.next
        
        while list1:
            curr.next = list1
            list1 = list1.next
            curr = curr.next

        while list2:
            curr.next = list2
            list2 = list2.next
            curr = curr.next
        
        return dummy.next
        