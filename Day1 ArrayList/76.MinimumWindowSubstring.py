"""
Example 1:

Input: s = "ADOBECODEBANC", t = "ABC"
Output: "BANC"
Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.

Example 2:

Input: s = "a", t = "a"
Output: "a"
Explanation: The entire string s is the minimum window.
"""

from typing import List
class Solution: 
    def minWindow(self, s: str, t: str) -> str: 
        if not s or not t or len(s) < len(t): 
            return ""

        start = 0 
        end = 0
        size = len(s)
        map = [0] * 128 
        count = len(t)


        for chat in t: 
            map[ord(chat)] += 1

        while end < size: 
            if map[ord(s[end])] > 0 : 
                count -= 1
            map[ord(s[end])] -= 1 


            end += 1     


