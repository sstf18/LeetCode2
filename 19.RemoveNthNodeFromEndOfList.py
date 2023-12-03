"""



"""

from typing import Optional


class ListNode: 
    def __init__(self, val=0, next=None) -> None:
        self.val = val 
        self.next = next

class Solution: 
    def removeNthFromEnd(self, head: Optional[ListNode], n: int)-> Optional[ListNode]:
        dummy_head = ListNode(next = head )
        slow = fast = dummy_head
        
        # fast should ahead of slow n steps
        for _ in range(n):
            fast = fast.next 

        while fast.next: 
            slow = slow.next 
            fast = fast.next 
        slow.next = slow.next.next 
        
        return dummy_head.next 
