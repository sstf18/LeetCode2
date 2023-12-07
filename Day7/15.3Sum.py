"""
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]]
such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Example 1:

Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Explanation: 
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
The distinct triplets are [-1,0,1] and [-1,-1,2].
Notice that the order of the output and the order of the triplets does not matter.
"""

from typing import List

class Solution: 
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = [] # create array
        nums.sort() # sort the value 

        # the first pointer: "i"
        for i in range(len(nums)): 
            if nums[i] > 0 :  # if > 0, return 
                return result 
            if i > 0 and nums[i] == nums[i - 1]: 
                continue

            left = i + 1 # the second pointer
            right = len(nums) -1 # the third pointer

            while left < right: 
                sum_ = nums[i] + nums[left] + nums[right]
                if sum_ > 0: 
                    right -= 1 
                elif sum_ < 0: 
                    left += 1 
                else: 
                    result.append([nums[i], nums[left], nums[right]])
                    while left < right and nums[right] == nums[right -1]: 
                        right -= 1       # if similar skip
                    while left < right and nums[left] == nums[left + 1]: 
                        left += 1 
                    right -= 1 
                    left += 1
        return result 