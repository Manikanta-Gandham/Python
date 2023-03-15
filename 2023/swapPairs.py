
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def swapPairs(self, head) -> ListNode:
        cur = res = ListNode(-1)
        cur.next = head
        while(cur.next != None and cur.next.next != None):
            a = cur
            b = cur.next
            c = cur.next.next

            a.next = c
            b.next = a
            cur = b
            cur = cur.next.next

        return res.next
    
sol = Solution()
input = ListNode(1,ListNode(2,ListNode(3,ListNode(4))))
sol.swapPairs(input)