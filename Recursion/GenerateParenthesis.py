def generateParenthesis(n):
  #if open count < n , you may add an open parenthesis
  #if close count < open count , you may add a closed parenthesis
  result = []
  stack = []
  def backtrack(openCount, closeCount):
    if openCount == closeCount == n:
      result.append(''.join(stack))
      return 
    if openCount < n:
      stack.append("(")
      backtrack(openCount + 1, closeCount)
      stack.pop()
    if closeCount < openCount:
      stack.append(")")
      backtrack(openCount , closeCount+1)
      stack.pop()
  backtrack(0,0)
  return result    
print(generateParenthesis(n=3))