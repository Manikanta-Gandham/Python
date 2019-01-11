# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        head = ListNode(0)
        current = head

        while l1 != None and l2!= None:
            if l1.val<l2.val:
                head.next = l1
                l1 = l1.next

            else:
                head.next = l2
                l2 = l2.next

            head = head.next

        if l1 == None:
            head.next = l2
        else:
            head.next = l1

        return current.next


l1 = ListNode(1)
l1.next = ListNode(4)
l1.next.next = ListNode(7)

l2 = ListNode(2)
l2.next = ListNode(5)
l2.next.next = ListNode(8)

sol = Solution()
sol.mergeTwoLists(l1,l2)