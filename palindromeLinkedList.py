# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        vals = []
        a = True
        while a:
            v = head.val
            vals.append(v)
            
            a = head.next != None
            if a:
                head = head.next
        high = -1
        low = 0
        
        while high < low:
            if vals[low] != vals[high]:
                return False
            high -= 1
            high += 1
            return True
            
            
        