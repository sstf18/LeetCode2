 
####

######

class Solution: 
    def isValidParentheses(self, s: str) -> bool: 
        stack = []
        for i in s: 
            if i == '(':
                stack.append(')')
            elif i == '[': 
                stack.append(']')
            elif i == '{':
                stack.append('}')
            elif not stack or stack[-1] != i: 
                return False 
        if not stack: 
            return True 
        else: 
            return False 