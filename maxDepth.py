# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
def maxDepth(root: TreeNode) -> int:
    if (root == None):
        return 0

    else:
        return max(1 + maxDepth(root.left), 1 + maxDepth(root.right))
    
if __name__ == '__main__':
    test = TreeNode(4, left = TreeNode(2),
                    right = TreeNode(7, left = TreeNode(6), right = TreeNode(8)))
    print(maxDepth(test))