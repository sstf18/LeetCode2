"""
gien two string s and t, return true if t is an anagram of s, and false otherwise. 

Example 1:

Input: s = "anagram", t = "nagaram"
Output: true

Example 2:

Input: s = "rat", t = "car"
Output: false
"""

class Solution: 
    def isAnagram(self, s: str, t: str)-> bool: 
        result = [0]* 26
        for i in s: 
            result [ord(i) - ord('a')] += 1
        for i in t: 
            result [ord(i) - ord('a')] -= 1
        for i in range(26):
            if result[i] != 0: 
                return False 
        return True 

solution = Solution()
test = solution.isAnagram('rat', 'ar')
print(test)
