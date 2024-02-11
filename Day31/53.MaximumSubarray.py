"""
Example 1:
Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: The subarray [4,-1,2,1] has the largest sum 6.

Example 2:
Input: nums = [1]
Output: 1
Explanation: The subarray [1] has the largest sum 1.

Example 3:
Input: nums = [5,4,-1,7,8]
Output: 23
Explanation: The subarray [5,4,-1,7,8] has the largest sum 23.
"""
from typing import List


class Solution: 
    def maxSubArray(self, nums: List[int]) -> int: 
        # maxNum = float('-inf')
        # count = 0 
        # for i in range(len(nums)): 
        #     count = 0 
        #     for j in range(i, len(nums)):
        #         count = count + nums[j]
        #         maxNum = max(count, maxNum)
        # return maxNum

        maxNum = float('-inf')
        count = 0 
        for i in range(len(nums)):
            
            count = count + nums[i]
            if count > maxNum: 
                maxNum = count
            if count <= 0 : 
                count = 0
        return maxNum

