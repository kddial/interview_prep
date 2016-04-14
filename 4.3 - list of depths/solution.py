import sys
sys.path.append("../data_structures")

from BTree import *
from LL import *

# started at 4 pm
# ended at least 6 pm
# duration 2 hours

# Solution to the question
# DFS approach: recrusive downwards while saving the depth value of each node

def solution(root):
	depthLL = []
	dfs_search_helper(root, 0, depthLL)
	return depthLL


def dfs_search_helper(root, depth, depthLL):

	if root:
		if len(depthLL) <= depth:
			treeLL = LLNode(root)
			depthLL.append(treeLL)
		else:
			treeLL = LLNode(root)
			depthLL[depth].addToTail(treeLL)

		dfs_search_helper(root.left, depth+1, depthLL)
		dfs_search_helper(root.right, depth+1, depthLL)





# Create sample Binary Tree
values = [0, 1, 2, 3, 4, 5, 6, 7, 8]
bt = BTree.createCompleteTree(values)

# print solution
bt_soln = solution(bt)
print("Printing solution for BT 1")
for llist in bt_soln:
	LLNode.printLL(llist)


# Create sample Binary Tree 2
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

n1.setChildren(n2, n3)
n2.setChildren(n4, n5)
n3.setChildren(n6, None)
n4.setChildren(n7, None)
n6.setChildren(n8, n9)
n9.setChildren(None, n10)

# print solution
bt2_soln = solution(n1)
print("Printing solution for BT 2")
for llist in bt2_soln:
	LLNode.printLL(llist)



