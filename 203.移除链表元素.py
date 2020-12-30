#
# @lc app=leetcode.cn id=203 lang=python3
#
# [203] 移除链表元素
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:

        while head and head.val == val:
            head = head.next

        pre, cur = head,head

        while cur:
            if cur.val == val:
                pre.next = cur.next
            else:
                pre = cur
        
            cur = cur.next
        
        return head


# @lc code=end
