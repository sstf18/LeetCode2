"""
given "head" of a singly linked list, reverse the list, and return the reversed list


Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1]

"""

from typing import Optional


class ListNode: 
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next 

class Solution: 
    def reverseList(self, head: Optional[ListNode], val: int)-> Optional[ListNode]:
        cur = head 
        pre = None

        while cur: 
            temp = cur.next 
            cur.next = pre
            pre = cur 
            cur = temp 
        return pre 


        