"""
given distinct integer "candidates" and a integers "target"
find all the combinations in any order

example
input: [2,3,6,7] target = 7
output: [[2,2,3], [7]]
"""

from typing import List


class Solution: 
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        self.result = []
        self.path = []
        self.traversal(candidates, target, 0)
        return self.result 
    def traversal(self, candidates, target, startIndex): 
        if sum(self.path ) == target:
            self.result.append(self.path.copy())
        for i in range(startIndex, len(candidates)):
            if sum(self.path) > target: 
                continue
            self.path.append(candidates[i])
            self.traversal(candidates, target, i)
            self.path.pop()

solution = Solution()
test = solution.combinationSum([2,3,6,7], 7)
print(test)
        
