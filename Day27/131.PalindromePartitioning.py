"""
input: string s = "aab"
output: [["a", "a", "b"], ["aa", "b"]] 

"""

from typing import List


class Solution: 
    def partition(self, s: str) -> List[List[str]]:
        self.result = []
        self.path = []
        self.traversal(s, 0)
        return self.result 
    def traversal(self, s, startIndex): 
        if startIndex == len(s):
            self.result.append(self.path[:])
            return 
        for i in range(startIndex, len(s)):
            if s[startIndex : i + 1] == s[startIndex : i + 1][::-1]:
                self.path.append(s[startIndex : i + 1])
                self.traversal(s, i + 1)
                self.path.pop()