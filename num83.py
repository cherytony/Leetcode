# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:

        if not head:
            return head

        pre, cur = head, head.next

        while True:

            while cur and cur.val == pre.val:
                cur = cur.next

            pre.next = cur
            pre = cur
            if not pre: break

            cur = cur.next

        return head