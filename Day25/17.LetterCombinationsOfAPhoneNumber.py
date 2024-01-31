"""
input: 
digits = '23'
output: 
["ad","ae","af","bd","be","bf","cd","ce","cf"]

{0: "", 1: "", 2:"abc",3:"def",4:"ghi",5:"jkl",6:"mno",7:"pqrs",8:"tuv",9:"wxyz"}
"""

from typing import List


class Solution: 
    def letterCombinations(self, digits: str) -> List[str]:
        self.result  = []
        self.s = ""
        characters = {0: "", 1: "", 2:"abc",3:"def",4:"ghi",5:"jkl",6:"mno",7:"pqrs",8:"tuv",9:"wxyz"}
        if not digits: 
            return []
        self.traversal(digits, characters, 0)
        return self.result 
    def traversal(self, digits, characters, index): 
        if len(self.s) == len(digits): 
            self.result.append(self.s[:])
            return 
        for i in characters[int(digits[index])]: 
            self.s += i 
            self.traversal(digits, characters, index+1)
            self.s = self.s[:-1]

