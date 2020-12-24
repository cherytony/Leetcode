#
# @lc app=leetcode.cn id=111 lang=python3
#
# [111] 二叉树的最小深度
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: TreeNode) -> int:

        if not root:
            return 0
        
        if not root.left and not root.right:
            return 1
        

        minDepth = 10**9

        if root.left:
            minDepth =  min(self.minDepth(root.left),minDepth)
        
        if root.right:
            minDepth =  min(self.minDepth(root.right),minDepth)
        

        return minDepth+1

# @lc code=end

