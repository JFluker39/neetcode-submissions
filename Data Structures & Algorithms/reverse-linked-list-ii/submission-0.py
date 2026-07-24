# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        i = 1
        dummy = node = ListNode()

        while i < left:
            node.next = head
            head = head.next
            i += 1
            node = node.next
        
        prev = None
        tmp = None
        while i <= right:
            tmp = head.next
            head.next = prev
            prev = head
            head = tmp
            i += 1

        node.next = prev
        j = 0
        while j < right - left + 1:
            node = node.next
            j += 1
        node.next = tmp
        return dummy.next    

        