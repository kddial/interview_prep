import sys
sys.path.append("../data_structures")
from BTree import *

def find_sums(root, value):
	
	# memoize all paths and their sum
	# paths are represented as a tuple of nodes
	paths = {}

	# empty path
	paths[()] = 0

	# recursive function to traverse through every node
	def traverse(root, path):
		if root:
			# get every sub-path that includes the parent node (and the empty path)
			for i in range((len(path) + 1), -1, -1):

				# create a new path to include current node
				parent_path = path[i:]
				new_path = parent_path + tuple([root])

				# calculate the sum of the new path by retreiving the sum of its parent path
				paths[new_path] = paths[parent_path] + root.data

			# traverse to child nodes
			# new path contains the root of the entire tree to the current node
			traverse(root.left, new_path)

			# prune right child if current node is greater than the value, based on the BST property
			if not(root.data > value):
				traverse(root.right, new_path)

	# call recursive function
	traverse(root, ())

	# find number of paths that have equal sum to the value
	count_paths = 0
	for path_sum in paths.values():
		if path_sum == value:
			count_paths += 1

	print_all_paths_sums(paths)

	return count_paths


def path_str(path):
	""" helper function to return string representation of paths """
	output = "PATH: "
	if path:
		for i in path:
			output += str(i.data) + " -> "
	else:
		output += "Empty"
	return output

def print_all_paths_sums(paths):
	for path in paths.keys():
		print("Sum: ", paths[path], "\t", path_str(path))



if __name__ == '__main__':
	
	# Create sample Binary Tree 
	n1 = BTree(6)
	n2 = BTree(4)
	n3 = BTree(20)
	n4 = BTree(-3)
	n5 = BTree(5)
	n6 = BTree(15)
	n7 = BTree(100)

	n1.setChildren(n2, n3)
	n2.setChildren(n4, n5)
	n3.setChildren(n6, n7)

	result = find_sums(n1, 15) # == 2
	print("Num of paths:", result)
	BTree.printBTree2(n1)




	# Create sample Binary Tree 2
	n1 = BTree(2)
	n2 = BTree(1)
	n3 = BTree(-1)
	n4 = BTree(-1)
	n5 = BTree(5)

	n1.setChildren(n2, n5)
	n2.setChildren(n3, None)
	n3.setChildren(n4, None)

	result = find_sums(n1, 1) # == 2
	print("Num of paths:", result)
	BTree.printBTree2(n1)