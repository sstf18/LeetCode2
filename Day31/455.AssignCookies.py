"""
Example 1:
Input: g = [1,2,3], s = [1,1]
Output: 1
Explanation: You have 3 children and 2 cookies. The greed factors of 3 children are 1, 2, 3. 
And even though you have 2 cookies, since their size is both 1, you could only make the child whose greed factor is 1 content.
You need to output 1.

Example 2:
Input: g = [1,2], s = [1,2,3]
Output: 2
Explanation: You have 2 children and 3 cookies. The greed factors of 2 children are 1, 2. 
You have 3 cookies and their sizes are big enough to gratify all of the children, 
You need to output 2.
"""

from typing import List


class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        count = 0 
        s.sort()
        g.sort()
        index = len(s) - 1
        # for i in range(0, len(g)):
        #     for j in range(0, len(s)):
        #         if j > 0 and s[j] == s[j -1]: 
        #             continue
        #         if s[j] >= g[i]:
        #             count += 1
        #             s[j] = - 1
        #             break          
        # return count 

        for i in range(len(g)-1, -1, -1): 
            if index >=0 and s[index] >= g[i]:
                count += 1 
                index -= 1
        return count 
