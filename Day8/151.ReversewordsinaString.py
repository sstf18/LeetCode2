"""

Example 1:

Input: s = "the sky is blue"
Output: "blue is sky the"
Example 2:

Input: s = "  hello world  "
Output: "world hello"
Explanation: Your reversed string should not contain leading or trailing spaces.

"""

class Solution: 
    def reverseWords(self,s:str) -> str: 
        new_s = s.split()
        left = 0 
        right = len(new_s) - 1
        while left < right: 
            new_s[left],new_s[right] = new_s[right], new_s[left]
            left +=1 
            right -= 1
        return ' '.join(new_s)

solution = Solution()
result = solution.reverseWords("the sky is blue")
print(result)