"""
Example 1:

Input: s = ["h","e","l","l","o"]
Output: ["o","l","l","e","h"]
Example 2:

Input: s = ["H","a","n","n","a","h"]
Output: ["h","a","n","n","a","H"]
"""
from typing import List


class Solution: 
    def reverseString(self, s: List[str])-> None: 
        left = 0 
        right = len(s)
        while left < right: 
            temp = s[left]
            s[left] = s[right-1]
            s[right - 1] = temp
            left += 1 
            right -=1  