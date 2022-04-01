class MaxStack:
    def __init__(self):
        self.stack = [] #adds all values to the stack etc
        self.maxStack = [] #keeps track of the max value 

    def push(self, x):
        self.stack.insert(0, x)
        if len(self.maxStack) == 0:
            self.maxStack.append(x)
        else:
            self.maxStack.insert(0, max(self.maxStack[0],x))    
    def pop(self):
        #pops the top value from the stack
        #bc you can't pop from an empty stack
        if len(stack):
            self.maxStack.pop(0)
            top =self.stack.pop(0)
        return top    

    def top(self):
        #returns the top value in the stack
        if len(self.stack):
            return self.stack[0]
        

    def peekMax(self):
        #returns he top value from the maxstack
        return self.maxStack[0]    

    def popMax(self):
        #this is the top value in the second stack which happens to be the max value
        max_element = self.maxStack.pop(0) 
        #bc you want to remove it from the stack, find it's index in the stack
        max_element_idx = self.stack.index(max_element)
        #pop the element from the 2 stacks using this index
        self.stack.pop(max_element_idx)
        self.maxStack.pop(max_element_idx) 
        #update the max element now
        if len(self.stack): #if stack is not empty
            self.maxStack[-1] =self.stack[-1]
            #need 2 understand what this 2 lines of code are trying to achieve
            for index in range(len(self.stack)-2, -1, -1):
                self.maxStack[index] = max(self.maxStack[index+1], self.stack[index])
        return max_element    




