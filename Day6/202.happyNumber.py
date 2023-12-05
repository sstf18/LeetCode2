"""
Example 1:

Input: n = 19
Output: true
Explanation:
1^2 + 9^2 = 82
8^2 + 2^2 = 68
6^2 + 8^2 = 100
1^2 + 0^2 + 0^2 = 1

"""

class Solution: 
    def getSum(self, n: int)-> int: 

        sum = 0 # this is very important 

        while n: 
            sum += (n%10)**2 
            n = n//10 
        return sum 

    def isHappy(self, n: int) -> bool: 
        record = set()
        while True: 
            n = self.getSum(n)
            if n == 1: 
                return True
            if n in record: 
                return False 
            record.add(n) 

