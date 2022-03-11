def validParenthesis(s):
    #create a stack
    stack = []
    #loop throough the string
    for char in s:
        #if the character is an open parenthesis, add it to the stack
        if char == "[" or char == "(" or char == "{":
            stack.append(char)
        #it's a closing parenthesis, therefore check whether the top
        # of the stack is the matching opening parenthesis while stack is not empty    
        elif char == "]" and stack and stack[-1] == "[":
            stack.pop()
        elif char == ")"and stack and stack[-1] == "(":
            stack.pop()
        elif char == "}" and stack and stack[-1] == "{":
            stack.pop() 
        else: #the top of the stack is not a matching open parenthesis => invalid
                return False 
    if stack: #if the stack is not empty , it's invalid
        return False
    else:
        return True 

print(validParenthesis( "{ ( [] ) }"))                             
               

#Using a hashmap 

def validP(s):
    hashmap = {')':'(',
    ']':'[',
    '}':'{'}
    stack = []
    for char in s:
        if char in hashmap.values():
            stack.append(char)
        elif char in hashmap.keys():
            if not stack or stack.pop() != hashmap[char]:
                return False
    return len(stack) == 0

print(validP("{ ( [] ) }"))



