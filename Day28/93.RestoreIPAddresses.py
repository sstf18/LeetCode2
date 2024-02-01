"""
find the valid IP address

Example 1:
Input: s = "25525511135"
Output: ["255.255.11.135","255.255.111.35"]

Example 2:
Input: s = "0000"
Output: ["0.0.0.0"]

Example 3:
Input: s = "101023"
Output: ["1.0.10.23","1.0.102.3","10.1.0.23","10.10.2.3","101.0.2.3"]

"""

from typing import List


class Solution: 
    def restoreIpAddresses(self, s: str) -> List[str]: 
        self.result = []
        self.path = []
        self.traversal(s, 0)
        return self.result

    def traversal(self, s, startIndex):
        if len(self.path) == 4 and startIndex == len(s) : 
            self.result.append('.'.join(self.path))
            return 
        if len(self.path) > 4: 
            return 
        for i in range(startIndex, min(startIndex + 3, len(s))):
            if self.is_valid(s, startIndex, i):
                self.path.append(s[startIndex: i+1])
                self.traversal(s, i+1)
                self.path.pop()

    def is_valid(self, s, start, end): 
        if start > end: 
            return False 
        if s[start] == 0 and start != end: 
            return False 
        num = int(s[start: end + 1])
        return 0 <= num <= 255
