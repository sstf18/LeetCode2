"""
Given the head of a linked list, return the node where
the cycle begins. if there is no cycle, return None. 

Input: head = [3,2,0,-4], pos = 1
Output: tail connects to node index 1

Input: head = [1], pos = -1
Output: no cycle
"""

from typing import Optional


class ListNode: 
    def __init__(self, val= 0, next = None):
        self.val = val 
        self.next = next 

class Solution: 
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = head 
        fast = head 

        while fast and fast.next: 
            slow = slow.next 
            fast = fast.next.next 

            if slow == fast: 
                slow = head 
                while slow != fast: 
                    slow = slow.next 
                    fast = fast.next 
                return slow 
        return None