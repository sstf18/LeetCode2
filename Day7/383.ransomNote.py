"""
Given two strings "ransomNote" and "magazine"
return "true" if "ransomNote" can be constructed by using the letters 
from "magazine" and "false" otherwise.

Example 1:

Input: ransomNote = "a", magazine = "b"
Output: false
Example 2:

Input: ransomNote = "aa", magazine = "ab"
Output: false
Example 3:

Input: ransomNote = "aa", magazine = "aab"
Output: true

"""

class Solution: 
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        record = [0]*26 
        for i in magazine: 
            record [ord(i) - ord('a')] += 1 
        for i in ransomNote: 
            record [ord(i) - ord('a')] -= 1 

        for i in range(26): 
            if record[i] < 0 : 
                return False 
        return True 

solution = Solution()
result = solution.canConstruct('aa', 'aab')
print(result)