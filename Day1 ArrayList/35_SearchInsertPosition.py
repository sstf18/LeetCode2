"""
Given a sorted array of distinct integers and a target value, return the index if the target is found. 
If not, return the index where it would be if it were inserted in order.

Example 1:

Input: nums = [1,3,5,6], target = 5
Output: 2
Example 2:

Input: nums = [1,3,5,6], target = 2
Output: 1
Example 3:

Input: nums = [1,3,5,6], target = 7
Output: 4

"""
from typing import List

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int: 
        left = 0 
        right = len(nums)
        middle = 0 
        while left < right: 
            middle = left + (right - left)//2
            if nums[middle] == target: 
                return middle 
            elif nums[middle] > target: 
                right = middle
            elif nums[middle] < target: 
                left = middle + 1
        return right     
         # this is the most important line, the reason to return "right"
         # beacause "right = middle", it is possible, the target is smaller than nums[middle], but bigger than right-1, 
         # so the right would be answer. 

solution = Solution()
result = solution.searchInsert([2,4,5,6,7,8], 3)
print(result)