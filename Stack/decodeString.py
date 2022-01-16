
def decodeString(s):
  stack = []
  for char in s:
      #if the character is not a closing bracket append it to your stack
      if char != ']':
          stack.append(char)
      else: #if it is 
        substring = ''
        k = ''
        
        while stack[-1] != '[': # you want to pop the stack top values till you get to a [ , this makes the substring
          substring = stack.pop() + substring 
        stack.pop()
        while stack and stack[-1].isdigit(): #pop the stack top if it is digit and add it to a string k
            k = stack.pop() + k
        stack.append(substring * int(k))
  return ''.join(stack)

  
print(decodeString('100[leetcode]'))