""""
Input: nums = [1,3,-1,-3,5,3,6,7], k = 3
Output: [3,3,5,5,6,7]

Explanation: 
Window position                Max
---------------               -----
[1  3  -1] -3  5  3  6  7       3
 1 [3  -1  -3] 5  3  6  7       3
 1  3 [-1  -3  5] 3  6  7       5
 1  3  -1 [-3  5  3] 6  7       5
 1  3  -1  -3 [5  3  6] 7       6
 1  3  -1  -3  5 [3  6  7]      7

"""

from collections import deque
from typing import List
class MyQueue: 
    def __init__(self):
        self.que = deque()

    def pop(self, value): 
        if self.que and value == self.que[0]:
            self.que.popleft()

    def push(self, value):
        if self.que and value > self.que[-1]:
            self.que.pop()
        self.que.append(value)

    def front(self):
        return self.que[0]

class Solution: 
    def maxSlidingWindow(self, nums:List[int], k: int) -> List[int]:
        que = MyQueue()
        result = []
        # run first k elements 
        for i in range(k):
            que.push(nums[i])
        result.append(que.front())

        # using k as start
        for i in range(k, len(nums)):
            # i - k is the left side of window 
            # i is the right side of window 
            que.pop(nums[i - k])
            que.push(nums[i])
            result.append(que.front())
        return result
