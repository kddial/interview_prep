import queue


class BTree:
	"""Binary Tree class"""


	def __init__(self, data):
		self.data = data
		self.left = None
		self.right = None


	def setChildren(self, left, right):
		self.left = left
		self.right = right


	@staticmethod
	def createCompleteTree(values):
		""" Create a binary complete tree given a list of values """

		root = BTree(values[0])
		BTree.createCompleteTreeHelper(values, root, 0)
		return root


	@staticmethod
	def createCompleteTreeHelper(values, root, i):
		""" Helper recursive function """

		left_i = (i*2)+1
		right_i = (i*2)+2

		if left_i < len(values):
			left = BTree(values[left_i])
			root.left = left
			BTree.createCompleteTreeHelper(values, left, left_i)

		if right_i < len(values):
			right = BTree(values[right_i])
			root.right = right
			BTree.createCompleteTreeHelper(values, right, right_i)


	@staticmethod
	def printBTree(root):
		""" Print descriptions of each node as a parent """
		
		if root:
			left = "_"
			right = "_"

			if root.left:
				left = root.left.data

			if root.right:
				right = root.right.data

			print("Parent: {}, Children: {}, {}".format(root.data, left, right))

			BTree.printBTree(root.left)
			BTree.printBTree(root.right)


	@staticmethod
	def printBTree2Helper(root):
		""" Print descriptions of each node as a parent """

		# 2d array of nodes of tree
		nodes = [[]]

		# BFS on nodes
		q = queue.Queue()
		q.put(root)
		
		# create a node to represent new lines
		NEWLINE = BTree("\n")
		q.put(NEWLINE)

		# begin BFS
		while(not q.empty()):
			current = q.get()
			nodes[-1].append(current)


			# at the end of every depth, create a new array for the next depth
			# and endqueue newline node, to repeat the process
			if(current == NEWLINE and q.qsize() > 1):
				nodes.append([])
				q.put(NEWLINE)
			else:
				if current:
					q.put(current.left)
					q.put(current.right)

		return nodes


	@staticmethod
	def printBTree2(root):
		nodes = BTree.printBTree2Helper(root)
		max_depth = len(nodes)

		for d, depth in enumerate(nodes):
			# print nodes
			for node in depth:

				if node:
					data = str(node.data)
				else:
					data = " "

				print("{0}{1}".format(" "* 2**(max_depth-d-1), data), end="")



if __name__ == '__main__':
	
	# Create sample Binary Tree 
	n1 = BTree(1)
	n2 = BTree(2)
	n3 = BTree(3)
	n4 = BTree(4)
	n5 = BTree(5)
	n6 = BTree(6)
	n7 = BTree(7)
	n8 = BTree(8)
	n9 = BTree(9)
	n10 = BTree(10)
	n11 = BTree(11)
	n12 = BTree(12)
	n13 = BTree(13)
	n14 = BTree(14)
	n15 = BTree(15)
	n16 = BTree(16)
	n17 = BTree(17)
	n18 = BTree(18)
	n19 = BTree(19)

	n1.setChildren(n2, n3)
	n2.setChildren(n4, n5)
	n3.setChildren(n6, n7)
	n4.setChildren(n8, n9)
	n5.setChildren(n10, n11)
	n6.setChildren(n12, n13)
	n7.setChildren(n14, n15)
	n8.setChildren(n16, n17)
	n9.setChildren(n18, n19)


	# BTree.printBTree(n1)

	BTree.printBTree2(n1)
	


