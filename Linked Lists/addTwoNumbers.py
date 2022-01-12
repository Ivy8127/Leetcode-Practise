# Time:  O(n)
# Space: O(1)
#
# You are given two linked lists representing two non-negative numbers. 
# The digits are stored in reverse order and each of their nodes contain a single digit.
# Add the two numbers and return it as a linked list.
#
# Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
# Output: 7 -> 0 -> 8
#
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
      output = ListNode(0)
      curr = output
      carry = 0
      while l1 or l2 or carry:
        v1 = l1.val if l1 else 0
        v2 = l2.val if l2 else 0
        total = v1 + v2 + carry
        carry = total // 10
        curr.next = ListNode( total % 10)

        curr = curr.next
        if l1:
          l1 = l1.next
        if l2:
          l2 = l2.next
      if carry > 0:
        curr.next = ListNode(carry)
      return output.next

#create linked list 1
a = ListNode(5)
a.next = ListNode(6) 
a.next.next = ListNode(4)

#create linked list 2
b = ListNode(2)
b.next = ListNode(4)
b.next.next = ListNode(3)
b.next.next.next = ListNode(3)
#create a solution class and call its methods
result = Solution().addTwoNumbers(a,b)
#return the values
print(result.val, result.next.val, result.next.next.val, result.next.next.next.val)
