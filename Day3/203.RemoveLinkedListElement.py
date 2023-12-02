"""
given the "head" of a linked List and integer "val"
remove all the nodes of the linked list that has "node.val == val", 
and return new head. 


Input: head = [1,2,6,3,4,5,6], val = 6
Output: [1,2,3,4,5]

Input: head = [], val = 1
Output: []
"""

# define singly-linked list. 
from typing import Optional


class ListNode: 
    def __init__(self, val=0 , next=None):
        self.val = val
        self.next = next

class Solution: 
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        dummy_head = ListNode(next = head)
        cur = dummy_head 
        while cur.next: 
            if cur.next.val == val: 
                cur.next = cur.next.next 
            else: 
                cur = cur.next 
        return dummy_head.next 

"""
solution = Solution()
result = solution.removeElements([1,2,6,3,4,5,6], 6)
print(result)

based on this, i learn that "head" is a linked list, not regular list, we need covert it into linked list. 
"""  

        