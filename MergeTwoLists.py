class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def mergeTwoLists(list1: ListNode, list2: ListNode) -> ListNode:
    # If either list is empty, return the non-empty one (or None if both are None)
    if (list1 == None):
        return list2
    elif (list2 == None):
        return list1

    # Initialise our head to the min(head1, head2)
    if (list1.val <= list2.val):
        head = list1
        list1 = list1.next
    else:
        head = list2
        list2 = list2.next
    
    i = head
    while ((list1 != None) and (list2 != None)):
        # Iterate through the nodes of list1 and list2 and select the smallest val at each iteration
        if (list1.val <= list2.val):
            i.next = list1
            list1 = list1.next
        else:
            i.next = list2
            list2 = list2.next
        i = i.next
    
    if (list1 == None):
        i.next = list2

    else:
        i.next = list1

    return head

if __name__ == '__main__':
    test1 = ListNode(0,ListNode(1,ListNode(2,ListNode(3))))
    test2 = ListNode(0,ListNode(2,ListNode(4,ListNode(5))))
    ans = mergeTwoLists(test1, test2)
    
    i = ans
    while (i.next != None):
        print(i.val)
        i = i.next
    print(i.val)