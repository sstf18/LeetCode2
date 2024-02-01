"""
Example 1:
Input: nums = [1,2,3]
Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]

Example 2:
Input: nums = [0]
Output: [[],[0]]

"""

from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.result = []
        self.path = []
        self.backTracking(nums, 0)
        return self.result 

    def backTracking (self, nums, startIndex): 
        self.result.append(self.path[:])
        if startIndex >= len(nums): 
            return 
        for i in range(startIndex, len(nums)):
            self.path.append(nums[i])
            print("nums[i]: ", nums[i])
            self.backTracking(nums, i+1)
            self.path.pop()