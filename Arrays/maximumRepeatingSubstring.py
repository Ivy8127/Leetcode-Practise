class Solution:
    def maxRepeating(self, sequence: str, word: str) -> int:
        count = 0
        for i in range(len(sequence)+1):
            if word * i in sequence:
                count = i
                
        return count        
        
            
        