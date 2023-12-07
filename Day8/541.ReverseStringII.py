"""
Example 1:
Input: s = "abcdefg", k = 2
Output: "bacdfeg"

Example 2:
Input: s = "abcd", k = 2
Output: "bacd"
"""

class Solution: 
    def reverseStr(self,s:str, k:int) -> str: 
        def reverseSubstr(text:str) -> str: 
            left = 0 
            right = len(text) - 1 
            while left <= right: 
                text[left], text[right] = text[right],text[left]
                left += 1 
                right -= 1 
            return text

        res = list(s)
        for i in range(0, len(s), 2*k):
            res[i:i+k] = reverseSubstr(res[i:i+k])
        return res
