"""
Given the heads of two singly linked-lists "headA" and "headB"
return the node at which the two lists intersect. 
if the two linked lists have no intersection at all, return null 

Input: intersectVal = 8, listA = [4,1,8,4,5], listB = [5,6,1,8,4,5], skipA = 2, skipB = 3
Output: Intersected at '8'

"""

from typing import Optional


class ListNode: 
    def __init__(self, val=0, next = None) -> None:
        self.val = val 
        self.next = next 

class Solution: 
    def getIntersectionNode(self, headA: ListNode, headB:ListNode)->Optional(ListNode): 
        lenA = lenB = 0 
        cur = headA
        while cur: 
            cur = cur.next 
            lenA += 1 
        cur = headB
        while cur: 
            cur = cur.next
            lenB += 1
        curA = headA 
        curB = headB 
        gap = lenB - lenA 

        if lenA > lenB: 
            curA, curB = curB, curA 
            lenA, lenB = lenB, lenA 
        
        for _ in range(gap):
            curB = curB.next 

        while curA: 
            if curA == curB: 
                return curA 
            else: 
                curA = curA.next
                curB = curB.next
        return None