#Optimal
# O(n)
# O(1)
#21/01/2022
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        fast = head #create a fast and slow pointer pointint to the head
        slow = head
        
        while(slow!= None and fast!=None and fast.next !=None):
            slow = slow.next
            fast = fast.next.next
            if fast == slow:
                return True
        return False


#Method 2 with a set
def hascycle(self,head):
	if head is None:
		return False
    cycle = set()
	curr = head
	while curr:
#check if current node is in cycle
		if curr in cycle:
			return True
		cycle.add(curr)
		curr = curr.next
	return False
