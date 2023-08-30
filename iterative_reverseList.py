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

def recursiveReverse(head):
    if not head:
        return head
    if not head.next:
        return head
    
    newHead = recursiveReverse(head.next)
    print(newHead.val)
    print(newHead.next)
    print(head.val)
    print(head.next)
    print(head.next.next)
    head.next.next = head
    head.next = None
        
    return newHead

if __name__ == '__main__':
    test = ListNode(0,ListNode(1,ListNode(2,ListNode(3))))
    ans = recursiveReverse(test)
    
    i = ans
    while (i.next != None):
        print(i.val)
        i = i.next
    print(i.val)