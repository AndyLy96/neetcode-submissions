# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        link = set()
        curr = head

        if not head:
            return False

        while curr.next:
            if curr in link:
                return True
            link.add(curr)
            curr = curr.next

        return False 