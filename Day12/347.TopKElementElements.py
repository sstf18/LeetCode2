""""
Given an integer array nums and an integer k, 
return the k most frequent elements. 
You may return the answer in any order.

Example 1:

Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]
Example 2:

Input: nums = [1], k = 1
Output: [1]

"""

import heapq
from typing import List 

class Solution: 
    def topKFrequent (self, nums: List[int], k: int)-> List[int]:
        map_ = {}
        for i in range(len(nums)):
            map_[nums[i]] = map_.get(nums[i], 0) + 1

        pri_que = []

        for key, freq in map_.items():
            heapq.heappush(pri_que, (freq, key))
            if len(pri_que) > k: 
                heapq.heappop(pri_que)
                
        result = [0] * k 
        for i in range(k-1, -1, -1):
            result[i] = heapq.heappop(pri_que)[1]
        return result