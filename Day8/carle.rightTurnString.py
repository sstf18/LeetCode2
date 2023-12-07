"""
例如，对于输入字符串 "abcdefg" 和整数 2，函数应该将其转换为 "fgabcde"。



"""

class Solution: 
    def rightTurnString(slef, s:str, k:int) -> str: 
        target_k = len(s) - k

        new_s = s[target_k:] + s[:target_k]
        return new_s

solution = Solution()
input1 = 'abcdef'
result = solution.rightTurnString(input1, 2)
print(result)
