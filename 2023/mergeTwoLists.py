class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
     def mergeTwoLists(self, list1, list2):
        #  headA = list1
        #  headB = list2
         res =  ListNode()
         temp = res
         if(list1 == None or list2== None):
             return list1 or list2
         while(list1 != None and list2 != None):
             if list1.val < list2.val:
                 res.next = list1
                 list1 = list1.next
             else:
                 res.next = list2
                 list2 = list2.next
             res = res.next
         if(list1 == None):
             res.next = list2
         if(list2 == None ):
             res.next = list1
         return temp.next
     
sol = Solution()
# print(sol.mergeTwoLists(None,None))

list1 = ListNode(1, ListNode(2, ListNode(4,None)))
list2 = ListNode(1,ListNode(3,ListNode(4,None)))
sol.mergeTwoLists(list1,list2)

         


         
         