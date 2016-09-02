# Question:
# Given an NxN matrix of positive and negative integers, 
# write code to find the sub matrix with the largest possible sum.


def getLargestSumMatrix(M):
	N = len(M)
	largestSum = 0
	largestSubmatrixTup = None

	# find all sub matrix permutations
	for x in range(0, N):
		for y in range(0, N):
			for w in range(1, N+1-x):
				for h in range(1, N+1-y):
					submatrixTup = (x, y, w, h)
					temp_sum = sumMatrix(submatrixTup, M)

					if temp_sum > largestSum:
						largestSum = temp_sum
						largestSubmatrixTup = submatrixTup
	return(largestSum)


# Return sum of sub matrix
#   x, y are top left coordinates of the sub matrix with respect to the full matrix
#   w is the width of the sub matrix
#   h is the height of the sub matrix
def sumMatrix(submatrixTup, M):
	(x, y, w, h) = (submatrixTup[0], submatrixTup[1], submatrixTup[2], submatrixTup[3])
	sum = 0
	for i in range(x, x+w):
		for j in range(y, y+h):
			sum = sum + M[i][j]
	return sum


def printMatrix(M):
	for row in M:
		for item in row:
			print('{0:4d}'.format(item), end="")
		print()

def printSubMatrix(submatrixTup):







M = [[1, 2, 3], 
	[4, 5, 6], 
	[7, 8, 9]]

if __name__ == '__main__':
	summ = getLargestSumMatrix(M)
	print(summ)
	printMatrix(M)

