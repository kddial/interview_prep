import sys
sys.path.append("../data_structures")
from BTree import *


def find_sum_path(root, path, curr_sum, value):
	# not a node
	if (not root):
		return 0

	num_paths = 0

	# append root to path and update sum
	path = path[:]
	path.append(root)
	curr_sum = curr_sum + root.data

	# if sum equals value, current root is the end of a valid path
	if (curr_sum == value):
		num_paths += num_paths + 1

	# if sum >= value, then pop of notes at the beginning
	# of path until sum is < value
	while(curr_sum >= value):
		curr_sum = curr_sum - path.pop(0).data

	# recurse on left child, and right child  <- can be optimized using binary search tree properties
	# return the total num of paths from root and children
	left_child = find_sum_path(root.left, path, curr_sum, value)
	right_child = find_sum_path(root.right, path, curr_sum, value)

	return (num_paths + left_child + right_child)


if __name__ == '__main__':
	

	# Create sample Binary Tree 2
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

	result = find_sum_path(n1, [], 0, 15)
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

	result = find_sum_path(n1, [], 0, 1)
	print("Num of paths:", result)

	BTree.printBTree2(n1)