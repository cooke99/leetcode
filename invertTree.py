# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def invertTree(root: TreeNode) -> TreeNode:
    if (root == None):
        return None

    else:
        L_node = invertTree(root.left)
        R_node = invertTree(root.right)
        root.left = R_node
        root.right = L_node

    return root

if __name__ == '__main__':
    test = TreeNode(4, left = TreeNode(2, left = TreeNode(1), right = TreeNode(3)),
                    right = TreeNode(7, left = TreeNode(6), right = TreeNode(8)))
    ans = invertTree(test)