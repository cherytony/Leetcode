#
# @lc app=leetcode.cn id=160 lang=python3
#
# [160] 相交链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        
        pa,pb = headA,headB

        

        while pa != pb:

            if not headA or not headB:
                return None

            pa = pa.next if pa else headB
            pb = pb.next if pb else headA
        
        return pa

        
# @lc code=end

