"""
nums = [1,2,2]
output: [[],[1],[1,2],[1,2,2],[2],[2,2]]

"""
from typing import List


class Solution: 
    def subsetsWithDup(self, nums: List[int])->List[List[int]]:
        self.result = []
        self.path = []
        nums.sort()
        self.backTracking(nums, 0)
        return self.result

    def backTracking(self, nums, startIndex): 
        self.result.append(self.path[:])
        for i in range(startIndex, len(nums)):
            if i > startIndex and nums[i] == nums[i-1]:
                continue 
            self.path.append(nums[i])
            self.backTracking(nums, i+1)
            self.path.pop()

solution = Solution()
test = solution.subsetsWithDup([1,2,2])
print(test)
