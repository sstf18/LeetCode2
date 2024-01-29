"""
Given n and k, return all the possible combinations of 
k numbers chosen from the range[1, n]
return in any order. 

example: 
Input: n = 4, k = 2
Output: [[1,2],[1,3],[1,4],[2,3],[2,4],[3,4]]
"""

class Solution: 
    def combine(self, n, k): 
        self.result = []
        self.path = []
        self.traversal(n,k, 1)
        return self.result 
    def traversal(self, n,k,startIndex):
        if len(self.path) == k: 
            self.result.append(self.path.copy())
            return 
        for i in range(startIndex, n+1):
            self.path.append(i)
            self.traversal(n,k, i+1)
            self.path.pop()