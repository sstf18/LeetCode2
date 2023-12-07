"""
Given four integer arrays nums1, nums2, nums3, and nums4 all of length n, 
return the number of tuples (i, j, k, l) 

Input: nums1 = [1,2], nums2 = [-2,-1], nums3 = [-1,2], nums4 = [0,2]
Output: 2
Explanation:
The two tuples are:
1. (0, 0, 0, 1) -> nums1[0] + nums2[0] + nums3[0] + nums4[1] = 1 + (-2) + (-1) + 2 = 0
2. (1, 1, 0, 0) -> nums1[1] + nums2[1] + nums3[0] + nums4[0] = 2 + (-1) + (-1) + 0 = 0
"""

from typing import List


class Solution: 
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        record = dict()
        for a in nums1: 
            for b in nums2: 
                if a+b in record: 
                    record[a+b] += 1
                else: 
                    record[a+b] = 1 

        count = 0 
        for c in nums3: 
            for d in nums4: 
                target = 0 - (c+d)
                if target in record: 
                    count += record[target]
        return count

solution = Solution()
result = solution.fourSumCount([1,2],[-2,-1],[-1,2],[0,2] )
print(result)