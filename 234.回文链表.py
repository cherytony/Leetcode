#
# @lc app=leetcode.cn id=234 lang=python3
#
# [234] 回文链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:

        look_up = []

        while head:
            look_up.append(head.val)
            head = head.next
        

        h,l = 0,len(look_up)-1

        while h<l:
            if look_up[h] != look_up[l]:
                return False
            
            h += 1
            l -= 1

        return True
# @lc code=end

