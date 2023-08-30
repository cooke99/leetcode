class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
def hasCycle(head: ListNode) -> bool:
    if (head == None):
        return False
    mem_dict = {}
    i = head
    while (i.next != None):
        if mem_dict.get(i,None):
            # O(1) read
            return True
        else:
            mem_dict[i] = True
        i = i.next
    return False

if __name__ == '__main__':
    test1 = ListNode(0,ListNode(1,ListNode(2,ListNode(3))))
    test1.next.next.next = test1.next
    
    print(hasCycle(test1))