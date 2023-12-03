"""
Given a linked list, swap every two adjacent nodes and return its head. 

Example1: 
Input: head = [1,2,3,4]
Output: [2,1,4,3]

Example 2:
Input: head = []
Output: []

Example 3:
Input: head = [1]
Output: [1]
"""
from typing import Optional

class ListNode: 
    def __init__(self, val = 0, next = None):
        self.val = val 
        self.next = next 

class Solution: 
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy_head = ListNode(next = head)
        cur = dummy_head

        while cur.next != None and cur.next.next != None: 

            temp1 = cur.next 
            temp2 = cur.next.next.next
            cur.next = cur.next.next 
            cur.next.next = temp1
            cur.next.next.next = temp2 
            cur = cur.next.next 
        return dummy_head.next 

        
    