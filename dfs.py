#Depth first search: Most fundamental graph/tree search algorithm
#Runs with a time complexity of O(V + E), building block in other algorithms
#uses - Count connected components, Det connectivity, Find bridges/ articulation points
#starts from Root node to the grestest depth before moving to the next
#Uses a stack DS///BFS uses the queue DS
#DISADV
#Possibility of re-occurence, infinite loop condition
#Complete within finite state space
#Time complexity O(n raised to m)
#space complexity O(bm)
#

#DFS algorithm using pre-order traversal

class Node:
	def __init__(self, value, left = None, right = None):
		self.value = value
		self.left = left
 		self.right = right

	def __str__(self):
		return "Node(" + str(self.value) + ")"

#Recursive approach _ Inbuilt stack
def walk(tree):
	if tree is not None:
		print(tree)
		walk(tree.left)
		walk(tree.right)

#Iterative method using own stack
def walk2(tree, stack):
	stack.append(tree)
	while len(stack) > 0:
		node = stack.pop()
		if node is not None:
			print(node)
			stack.append(node.right)
			stack.append(node.left) 
