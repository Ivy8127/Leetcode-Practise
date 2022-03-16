#reverse singly linked list
# 2 -> 3 -> 5
class LinkedList:
    def __init__(self, next = None,val = 0):
        self.next = next
        self.val = val

# 2 3 5
list1 = LinkedList(2)
list1.next = LinkedList(3)

def reverseLinkedList(list1):
    prev= None
    curr = list1
    while curr:
        next_node = curr.next
        curr.next = prev
        prev = curr
        curr = next_node
    return prev #return the head of the reversed linked list

# 1 2 3
# 2 4 5 6
# 1 2 2  3 4 5 6  

def combineLinkedLists(list1, list2):
    list3 = LinkedList()
    curr = list3

    while list1 or list2:
        if list1:
            next_val = list1.val
            list1 = list1.next
        elif list2:
            next_val = list2.val
            list2 = list2.next
        else:
            #both have values
            if list1.val <= list2.val:
                next_val = list1.val
                list1= list1.next
            else:
                next_val = list2.val
                list2 = list2.next
        #update our 3rd linked list pointers
        curr.next = ListNode(next_val)
        curr = curr.next
    return list3.next    



                            
