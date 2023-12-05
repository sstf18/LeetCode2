""""
Given two integer arrays nums1 and nums2, return an array of their intersection.

Example 1:
Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2]

Example 2:
Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [9,4]
Explanation: [4,9] is also accepted.
"""

from typing import List


class Solution: 
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        set_nums1 = set(nums1)
        result = set()
        for i in nums2: 
            if i in set_nums1: 
                result.add(i)
        return list[result]     #the type of result is list, whic is sorted answer
        # return result      # this is set, which is unsorted result. 