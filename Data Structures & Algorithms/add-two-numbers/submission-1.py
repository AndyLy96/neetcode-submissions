# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        node = ListNode(0, None)
        dummy = node
        carry = 0
        while l1 or l2 or carry != 0:
            value1 = l1.val if l1 else 0
            value2 = l2.val if l2 else 0
            add = value1 + value2 + carry
            node1 = add % 10
            carry = add // 10
            node.next = ListNode(node1, None)
            node = node.next
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next       
        return dummy.next
                