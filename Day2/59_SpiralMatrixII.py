"""
Given a positive integer n, generate an n x n matrix filled with elements from 1 to n^2 in spiral order.

Input: n = 3
Output: [[1,2,3],[8,9,4],[7,6,5]]

Example 2:

Input: n = 1
Output: [[1]]
"""

from typing import List
class Solution: 
    def generateMatrix(self, n:int) ->List[List[int]]:
        result = [[0]*n for _ in range(n)]
        i = 0 
        j = 0 
        loop = n // 2
        mid = n // 2
        count = 1

        for offset in range(1, loop+1):
            for k in range(j, n-offset):
                result[i][k] = count
                count += 1 
            for k in range(i, n-offset):
                result[k][n-offset] = count
                count += 1
            for k in range(n-offset, j, -1):
                result[n-offset][k] = count 
                count += 1
            for k in range(n-offset, i, -1):
                result[k][j] = count
                count += 1 
            
        if n%2 != 0: 
            result[mid][mid] = count 
        
        return result 

"""
the most important parts are that setting "loop" need to figure out weather "n" is even or odd
if "n" is odd, the result[mid][mid] directly = count, no need to use loop 
then we can know that the loop comes from "n//2", which is used in the first loop.
"""

solution = Solution()
matrix = solution.generateMatrix(1)
print(matrix)