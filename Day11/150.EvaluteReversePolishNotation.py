"""

Example 1:

Input: tokens = ["2","1","+","3","*"]
Output: 9
Explanation: ((2 + 1) * 3) = 9
Example 2:

Input: tokens = ["4","13","5","/","+"]
Output: 6
Explanation: (4 + (13 / 5)) = 6

"""

from operator import add, sub, mul
from typing import List

class Solution: 
    op_map = {'+': add, '-': sub, '*':mul, '/': lambda x, y: int(x/y)}
    def evalRPN(self, tokens: List[str]) -> int: 
        stack = []
        for i in tokens: 
            if i not in {'+', '-', '*', '/'}: 
                stack.append(i)
            else: 
                op2 = stack.pop()
                op1 = stack.pop()
                stack.append(self.op_map[i](op1, op2))
        return stack.pop()

