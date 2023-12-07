"""
样例输入：a1b2c3

样例输出：anumberbnumbercnumber

replace '1,2,3,4,...' into 'number'
"""
class Solution: 
    def replaceNumber (self, s: str)-> str: 
        res=list(s)
        for i in range(len(s)):
            if res[i] in ['1','2','3','4','5','6','7','8','9','0']:
                res[i] = "number"
        return ''.join(res)

solution = Solution()
result = solution.replaceNumber("a1b2c3")
print(result)