# q1.py

def Braces(values):

	# array of open braces, and close braces
	open_braces = ["(", "{", "["]
	close_braces = [")", "}", "]"]
	output = []

	for value in values:
		# queue of open braces and missing close braces
		open_queue = []
		close_queue = []

		# traverse characters
		for char in value:
			# if matches any open braces, append to queue
			if char in open_braces:
				open_queue.append(char)

			# if matches any close braces, check if it closes the last open brace on queue
			if char in close_braces:
				if helper_check_mactching_close_brace(open_queue, char, open_braces, close_braces):
					# remove open brace from queue
					open_queue.pop(-1)
				else:
					# if close brace does not match, then it is a missing close brace and the entire value is unbalanced
					close_queue.append(char)
					break

		# end of traversal, if there are still open braces on queue, or missing close braces, then the value is unbalanced
		if len(open_queue) == 0 and len(close_queue) == 0:
			output.append("YES")
		else:
			output.append("NO")
	return output

# Helper function to check for matching close brace and last open brace
# return True if the close brace matches the last open brace
# return False otherwise
def helper_check_mactching_close_brace(queue, curr_close_brace, open_braces, close_braces):
	# no open brace on queue, return false
	if len(queue) < 1:
		return False

	# find the indexes of the open brace and close brace with reference to the array of all braces
	# if indexes match, then they are matching braces
	top_open_brace = queue[-1]
	open_index = open_braces.index(top_open_brace)
	close_index = close_braces.index(curr_close_brace)

	return (open_index == close_index)




values = ['{}[]()', '{[}]'] # yes, no
values.append("((())") # no
values.append("((()))") # yes
values.append("(") # no
values.append(")") # no

print(values, Braces(values))