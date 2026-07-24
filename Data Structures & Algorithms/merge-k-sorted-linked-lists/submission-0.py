# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        if not lists:
            return
        arr = []
        for l in lists:
            cur = l
            while cur:
                arr.append(cur.val)
                cur = cur.next
        
        arr.sort()
        dummy = ListNode()
        cur = dummy
        for i in range(len(arr)):
            cur.next = ListNode(arr[i])
            cur = cur.next
        return dummy.next 
