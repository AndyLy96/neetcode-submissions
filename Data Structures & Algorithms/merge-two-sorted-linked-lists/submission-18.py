# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1 and not list2:
            return None
        
        if list1 and not list2:
            return list1
        if list2 and not list1:
            return list2

        curr1, curr2 = list1, list2
        res = []

        while curr1 and curr2:
            if curr1.val == curr2.val:
                res.append(curr1.val)
                res.append(curr2.val)
                curr1 = curr1.next
                curr2 = curr2.next
            elif curr1.val < curr2.val:
                res.append(curr1.val)
                curr1 = curr1.next
            elif curr2.val < curr1.val:
                res.append(curr2.val)
                curr2 = curr2.next

        ans = ListNode(res[0])

        curr = ans
        for n in range(1,len(res)):
            node = ListNode(res[n])
            curr.next = node    
            curr = curr.next    
        
        if curr1:
            curr.next = curr1
        if curr2:
            curr.next = curr2

        return ans
