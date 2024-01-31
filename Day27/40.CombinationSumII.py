"""
candidate numbers [10,1,2,7,6,1,5]
target  = 8 

find all unique combinations in candidates:
[
[1,1,6],
[1,2,5],
[1,7],
[2,6]
]
"""

from typing import List


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        self.result = []
        self.path = []
        self.sorted_Candidates = self.sortCandidates(candidates)
        self.traversal(self.sorted_Candidates, target, 0)
        return self.result 

    def sortCandidates(self, candidates: List[int]): 
        for i in range(0, len(candidates)):
            for j in range(i+1, len(candidates)):
                if candidates[i] >= candidates[j]: 
                    temp = candidates[j]
                    candidates[j] = candidates[i]
                    candidates[i] = temp
        return candidates

    def traversal(self, candidates, target, startIndex):
        if sum(self.path) == target: 
            self.result.append(self.path.copy())
            return 
        for i in range(startIndex, len(candidates)) : 
            if sum(self.path) > target: 
                continue 
            if i > startIndex and candidates[i] == candidates[i-1]:
                continue
            self.path.append(candidates[i])
            self.traversal(candidates, target, i+1)
            self.path.pop()
