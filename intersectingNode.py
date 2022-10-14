#Traverse the two lists to the intersection point
#Go through both lists to the end then set the pointers to the beginning 
#of the other list, a different pointer from the one you're manmipulating

class ListNode:
	def __init__(self, x):
		self.val = x
		self.next = None

class Solution:
	 def getIntersectingNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
		l1, l2 = headA, headB
		while l1 != l2:
			l1 = l1.next if l1 else headB
			l2 = l2.next if l2 else headA
		return l1


