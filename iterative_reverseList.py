# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverseList(head: ListNode) -> ListNode:
    if (head == None):
        # Empty list case
        return None
    
    node = head
    ans = ListNode(next = None) # Initialise deepest node
    while (node.next != None):
        ans.val = node.val # Set current node val
        ans = ListNode(next = ans)
        node = node.next
    ans.val = node.val
    return ans

if __name__ == '__main__':
    test = ListNode(0,ListNode(1,ListNode(2,ListNode(3))))
    ans = reverseList(test)
    
    i = ans
    while (i.next != None):
        print(i.val)
        i = i.next
    print(i.val)