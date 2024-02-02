"""
input: 
nums = [4,6,7,7]
output: 
[[4,6],[4,6,7],[4,6,7,7],[4,7],[4,7,7],[6,7],[6,7,7],[7,7]]

Input: nums = [4,4,3,2,1]
Output: [[4,4]]

idea: looks similiar with sumII, but difference, non-decreasing 
"""
from typing import List


class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        self.result = []
        self.path = []
        self.backTracking(nums, 0)
        return self.result

    def backTracking(self, nums, startIndex):
        if len(self.path) > 1: 
            self.result.append(self.path[:])
        uset = set()
        for i in range(startIndex, len(nums)):
            if nums[i] in uset or (self.path and nums[i] < self.path[-1]): 
                continue 
            self.path.append(nums[i])
            self.backTracking(nums, i+1)
            self.path.pop()

solution = Solution()
test = solution.findSubsequences([4,4,3,2,1])
print(test)
