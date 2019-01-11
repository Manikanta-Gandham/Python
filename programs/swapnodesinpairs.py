class Solution:
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        a = head
        b = head.next
        c = b.next
        while a!= None and b !=None :
            a.next = c
            b.next = a

