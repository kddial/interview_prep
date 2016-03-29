class BTreeNode:
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

		root = BTreeNode(values[0])
		BTreeNode.createCompleteTreeHelper(values, root, 0)
		return root


	@staticmethod
	def createCompleteTreeHelper(values, root, i):
		""" Helper recursive function """

		left_i = (i*2)+1
		right_i = (i*2)+2

		if left_i < len(values):
			left = BTreeNode(values[left_i])
			root.left = left
			BTreeNode.createCompleteTreeHelper(values, left, left_i)

		if right_i < len(values):
			right = BTreeNode(values[right_i])
			root.right = right
			BTreeNode.createCompleteTreeHelper(values, right, right_i)

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

			BTreeNode.printBTree(root.left)
			BTreeNode.printBTree(root.right)










