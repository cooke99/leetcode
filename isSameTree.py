# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
def isSameTree(p: TreeNode, q: TreeNode) -> bool:
    if ((p == None) and (q == None)):
        return True

    elif ((p == None) and (q != None)):
        return False

    elif ((p != None) and (q == None)):
        return False

    elif (p.val != q.val):
        return False

    else:
        return (isSameTree(p.left, q.left)) and (isSameTree(p.right, q.right))

if __name__ == '__main__':
    p = TreeNode(4, left = TreeNode(2, left = TreeNode(1), right = TreeNode(3)),
                    right = TreeNode(7, left = TreeNode(6), right = TreeNode(8)))
    q = TreeNode(4, left = TreeNode(2, left = TreeNode(1), right = TreeNode(3)),
                    right = TreeNode(7, left = TreeNode(6), right = TreeNode(8)))
    
    print(isSameTree(p,q))