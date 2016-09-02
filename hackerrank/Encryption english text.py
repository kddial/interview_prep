# sentence with no spaces
# ex) haveaniceday
# output encoded message
# ex) hae and via ecy
# https://www.hackerrank.com/challenges/encryption

import math

# text = input()
text = "haveaniceday"

def encode(text):
	# find length L
	L = len(text)

	# find dimension options for grid to follow this constraint:
	# floor(sqrt(L)) <= rows <= cols <= ceiling(sqrt(L)) 
	lsqrt = math.sqrt(L)

	# let rows and cols equal floor(sqrt(L)), and incremently increase dimension
	# size until it satisfies the length of text
	rows = math.floor(lsqrt)
	cols = math.floor(lsqrt)

	# there are only 3 possible dimensions:
	# floor(sqrt(L)) x floor(sqrt(L)), floor(sqrt(L)) x floor(sqrt(L))+1, floor(sqrt(L))+1 x floor(sqrt(L))+1
	# let sqrt(L) = 3.4
	# possible dimensions are 3x3, 3x4, 4x4
	dimensions = [(rows, cols), (rows, cols+1), (rows+1, cols+1)]
	final_dim = dimensions[0]

	# find the dimension that gives the min area to match length of text
	# therefore, min(dimensions) >= L
	for dim in dimensions:
		if (dim[0] * dim[1] >= L):
			final_dim = dim
			break

	# transform text to grid
	grid = []
	col_counter = 0
	row_counter = 0

	for i in range(len(text)):

		if col_counter == 0:
			# append array for new row
			grid.append([text[i]])
			col_counter += 1

		elif col_counter == dim[1]-1:
			# restart col_counter at end of row
			grid[row_counter].append(text[i])
			col_counter = 0
			row_counter += 1

		else:
			# continue appending to current row
			grid[row_counter].append(text[i])
			col_counter += 1


	# transform grid to output, grab letters per column, and seperate columns by spaces
	output = ""

	for y in range(len(grid[0])):
		for x in range(len(grid)):
			if len(grid[x]) > y:
				output += grid[x][y]
		output += " "

	# remove the last space
	output = output[:-1]
	return output

print(encode(text))

#4:56 pm to 5:25 pm
# 30 mins so far!

# need 10 more mins, time it!
# 5 mins to test it!
# try for 45 mins in total!

# begin again at 3:14 am
# done at 3:26 am
# really done at 3:37 
# 23 mins

# total 43 mins