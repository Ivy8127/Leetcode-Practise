class Solution:
    def calculate(self, s: str) -> int:
        stack, curr_num , op = [], 0, "+"
        nums = set([str(i) for i in range(10)]) #numbers from 0 -9
        operators = ["+","-","*","/"]
        for i in range(len(s)):
            char = s[i]
            if char in nums:
                curr_num = curr_num * 10 + int(char)
            
            if char in operators or i == len(s)-1:
                if op == "+":
                    stack.append(curr_num)
                elif op == "-":
                    stack.append(-curr_num)
                elif op == "*":
                    stack[-1] *= curr_num
                elif op == "/":
                    stack[-1] = int(stack[-1] / curr_num)
                op = char
                curr_num = 0
        return sum(stack)           
        