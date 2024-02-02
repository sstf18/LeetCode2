"""
Example 1:
Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]

Example 2:
Input: nums = [0,1]
Output: [[0,1],[1,0]]

"""
from typing import List


class Solution: 
    def permute(self, nums: List[int]) -> List[List[int]]:
        self.result = []
        self.path = []
        self.backTracking(nums, [False]* len(nums))
        return self.result

    def backTracking(self, nums, used ): 
        if len(self.path) == len(nums):
            self.result.append(self.path[:])
            return 
        for i in range(len(nums)): 
            if used[i]: 
                continue 
            used[i] = True 
            self.path.append(nums[i])
            self.backTracking(nums, used)
            used[i] = False 
            self.path.pop()

solution = Solution()
test = solution.permute([1,1,2])
print(test)
        