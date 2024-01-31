"""
given k numbers that 
the sum of k nums equal to n 
for example: k = 3, n = 9 (find 3 numbers whose sum is 9)

output: 
1+2+6 = 9
1+3+5 = 9 
2+3+4 = 9
"""

class Solution: 
    def combinationSum3(self, k, n): 
        self.result = []
        self.path = []
        self.traversal(k, n, 1)
        return self.result 
    def traversal(self, k, n, Startindex):
        if sum(self.path) > n: 
            return 
        if sum(self.path) == n and len(self.path) == k: 
            self.result.append(self.path[:])
            return 
        for i in range(Startindex, 9 - (k - len(self.path))+2):
            self.path.append(i)
            self.traversal(k,n,i+1)
            self.path.pop()