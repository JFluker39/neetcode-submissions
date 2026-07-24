# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        d = {}
        cur = head
        i = 0
        while cur:
            d[i] = cur
            cur = cur.next
            i += 1
        print(d[i - n].val)
        if len(d) == 1:
            return None
        
        if i - n == 0:
            del d[i - n]
            return d[i - n + 1]
        else:
            d[i - n - 1].next = d[i - n].next
            del d[i - n]
        return d[0]