"""
Example 1:
Input: nums = [1,1,2]
Output:
[[1,1,2],
 [1,2,1],
 [2,1,1]]

Example 2:
Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]

"""
from typing import List

# this problem combined the 40 and 46
class Solution: 
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        self.result = []
        self.path = []
        self.backTracking(nums, [False]*len(nums))
        return self.result

    def backTracking(self, nums, used): 
        if len(self.path) == len(nums):
            self.result.append(self.path[:])
            return 
        # prevent duplicate using: set()
        uset = set()
        
        for i in range(len(nums)):
            if used[i]: 
                continue 
            if nums[i] in uset: 
                continue 

            used[i] = True
            uset.add(nums[i])
            self.path.append(nums[i])
            self.backTracking(nums, used)
            used[i] = False 
            self.path.pop()