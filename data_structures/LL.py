class LLNode:
	""" Linked List class """
	
	def __init__(self, data):
		self.data = data;
		self.next = None;

	@staticmethod
	def getTail(root):
		if root:
			if root.next:
				return LLNode.getTail(root.next)
			else:
				return root


	def addToTail(self, node):
		tail = LLNode.getTail(self)
		tail.next = node


	@staticmethod
	def printLL(node):
		if node:
			# Important, printing the data of the binary node !!
			print(str(node.data.data) + " -> ", end="")
			LLNode.printLL(node.next)
		else:
			print("END")

