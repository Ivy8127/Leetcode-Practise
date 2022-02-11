class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        output = []
        digitMap = {
            '2':'abc',
            '3' :'def',
            '4' : 'ghi',
            '5': 'jkl',
            '6' :'mno',
            '7': 'pqrs',
            '8':'tuv',
            '9':'wxyz'
        }
        def backtrack(index, currStr):
            #base case 
            if len(currStr) == len(digits):
                output.append(currStr)
                return
            for char in digitMap[digits[index]]:
                backtrack(index+1, currStr + char)
                
       #edge case
        if digits:
            backtrack(0, "")
        return output    