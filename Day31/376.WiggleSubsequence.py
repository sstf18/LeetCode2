"""
Example 1:
Input: nums = [1,7,4,9,2,5]
Output: 6
Explanation: The entire sequence is a wiggle sequence with differences (6, -3, 5, -7, 3).

Example 2:
Input: nums = [1,17,5,10,13,15,10,5,16,8]
Output: 7
Explanation: There are several subsequences that achieve this length.
One is [1, 17, 10, 13, 10, 16, 8] with differences (16, -7, 3, -3, 6, -8).

Example 3:
Input: nums = [1,2,3,4,5,6,7,8,9]
Output: 2
"""
from typing import List


class Solution:
    def wiggleMaxLength(nums: List[int]) -> int: 
        if len(nums) <= 1: 
            return len(nums)
        curDiff = 0 
        preDiff = 0 
        result =  1
        print("len(nums): ", len(nums))

        for i in range(len(nums) - 1): 
            print("i", i)
            curDiff = nums[i + 1] - nums[i]
            if (curDiff * preDiff) <= 0 and curDiff != 0: 
                result += 1 
                preDiff = curDiff

        return result 

solution = Solution 
test = solution.wiggleMaxLength([1,7,4,9,2,5])
print(test)