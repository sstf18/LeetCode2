"""
Given an array of integers nums sorted in non-decreasing order, 
find the starting and ending position of a given target value.
If target is not found in the array, return [-1, -1].

Example 1:

Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]
Example 2:

Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]
Example 3:

Input: nums = [], target = 0
Output: [-1,-1]

"""

from typing import List


class Solution: 
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        # using binary Search find the target
        def binarySearch(nums: List[int], target: int) -> int: 
            left, right = 0, len(nums)
            middle = 0
            while left < right: 
                middle = left + (right - left)//2
                if nums[middle] > target: 
                    right = middle 
                elif nums[middle] < target: 
                    left = middle + 1 
                else: 
                    return middle 
            return -1 
        
        # based on index of finding target to find the left side and right side.
        index = binarySearch(nums, target)
        left, right = index, index 

        # find all the left side of target, then record the index of left
        while left-1 >= 0 and nums[left-1] == target: 
            left -= 1 
        # similar with left side, this is right side. 
        while right+1 < len(nums) and nums[right+1] == target: 
            right += 1
        return [left, right]




