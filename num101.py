# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:

    def isSymmetric(self, root: TreeNode) -> bool:
        if not root:
            return True

        def check(node1, node2):

            if not node1 and not node2:
                return True

            if node1 and node2 and node1.val == node2.val:
                return check(node1.left, node2.right) and check(node1.right, node2.left)

            return False

        return check(root, root)



