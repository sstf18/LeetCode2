"""
Given an array nums of n integers, 
return an array of all the unique quadruplets [nums[a], nums[b], nums[c], nums[d]] 
such that:
0 <= a, b, c, d < n
a, b, c, and d are distinct.
nums[a] + nums[b] + nums[c] + nums[d] == target

Example 1:

Input: nums = [1,0,-1,0,-2,2], target = 0
Output: [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]
Example 2:

Input: nums = [2,2,2,2,2], target = 8
Output: [[2,2,2,2]]
"""
from typing import List


class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        result = []
        n = len(nums)

        for i in range(n): 
            if nums[i] > 0 and nums[i] > target and target > 0: 
                break 
            if nums[i] == nums[i - 1]: 
                continue 
            for k in range(i+1, n): 
                if k > i + 1 and nums[i] + nums[k] > target and target > 0:   
                    break 
                if nums[k] == nums[k -1]: 
                    continue 
                left = k + 1 
                right = n - 1 
                while left < right: 
                    s = nums[i] + nums[k] + nums[left] + nums[right]
                    if s > target: 
                        right -= 1
                    elif s < target: 
                        left += 1 
                    else: 
                        result.append([nums[i], nums[k], nums[left], nums[right]])
                        while left < right and nums[left] == nums[left + 1]: 
                            left += 1
                        while left < right and nums[right] == nums[right - 1]: 
                            right -= 1 
                        left += 1 
                        right -= 1
        return result 
