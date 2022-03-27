#The idea is to create a list/queue that will hold the values of the inorder traverseal 
#of the tree
#Remember that the inorder traversal of a tree returns a sorted list/queue
#So next() in a queue , returns the left most element in the queue
# which happens to be the smallest value bc its sorted. 
#Therefore you can use the popleft() function which returns the leftmost popped number
#or in a list , have a pointer at -1 which increments by one when the next function
# is called and return the value at that index
#haNext() returns true if the list is not empty otherwise false
# / check whether when you increment the index by 1 if it's less than the
# length of the array then return true else return false
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
      self.val = val
      self.left = left
      self.right = right

class BSTIterator:

  def __init__(self, root: TreeNode):
    #initialize an empty list that will hold the values of the inorder traversal
    self.inorder_list = []
    #create an index pointer
    self.index = -1
    #call the inorder method on the root
    self.inorder(root)
    def inorder(self,root):
      if root is None:
        return
      else:
        self.inorder(root.left)
        self.inorder_list.append(root.val)
        self.inorder(root.right)
    def next(self):
      #The index pointer is at -1 , you want to increment it , then return the it's value in the list
      self.index += 1
      return self.inorder_list[self.index] #this will return the current index in the list

    def hasnext(self):
      if self.index+1 < len(self.inorder_list):
        return True
      else:
        return False

root = TreeNode()
obj = BSTIterator(root)
obj.inorder([])
# param_1 = obj.next()
# param_2 = obj.hasNext()                 
