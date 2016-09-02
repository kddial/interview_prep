import queue


class Node:
	# initialize with data and children
	def __init__(self, data):
		self.data = data
		self.children = []
		self.visited = False

	@classmethod
	def hasChildren(self):
		return (len(self.children) > 0)

	def addChild(self, node):
		self.children.append(node)

# initailize node
n1 = Node(1)
n2 = Node(2)
n3 = Node(3)
n4 = Node(4)
n5 = Node(5)
n6 = Node(6)
n7 = Node(7)

# add child: n1 -> n2 -> n3 -> n4 -> n5 -> n6 -> n7
n1.addChild(n2)
n2.addChild(n3)
n3.addChild(n4)
n4.addChild(n5)
n5.addChild(n6)
n6.addChild(n7)

q = queue.Queue()
q.put(1)
print(q.get())





def routeExist(node1, node2):


	# queue 
	q = queue.Queue()
	q.put(node1)


	# keep checking until queue is empty
	while not (q.empty()):
		top = q.get()

		# check if top item is node2
		if top == node2:
			return True
		else:
			# add children to queue
			for child in top.children:
				q.put(child)

	return False
	


# bidrectional BFS
def routeExist2(node1, node2):

	# queue 1
	q1 = queue.Queue()
	q1.put(node1)

	# queue 2
	q2 = queue.Queue()
	q2.put(node2)

	# keep checking until queue is empty
	while (not (q1.empty())) or (not (q2.empty())):

		# bfs for node 1
		top = q1.get()
		if top.visited:
			return True
		else:
			# add children to queue
			top.visited = True
			for child in top.children:
				q1.put(child)

		# bfs for node 2
		top = q2.get()
		if top.visited:
			return True
		else:
			# add children to queue
			top.visited = True
			for child in top.children:
				q2.put(child)


	return False







if __name__ == '__main__':
	print(routeExist(n1, n7))

