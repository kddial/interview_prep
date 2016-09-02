# Question:
# Given an NxN matrix of positive and negative integers, 
# write code to find the sub matrix with the largest possible sum.



# How to optimize?
# Memoization of the sums of each sub matrix
# Dynamically calculate sum by using their submatrixes' sum

def getLargestSumMatrix(M):
	N = len(M)
	largestSum = 0
	largestSubmatrix = []

	# find all sub matrix permutations
	for x in range(0, N):
		for y in range(0, N):
			for w in range(1, N+1-x):
				for h in range(1, N+1-y):
					subMatrix = getSubMatrixZeros(x, y, w, h, M)
					temp_sum = sumMatrix(subMatrix)

					if temp_sum > largestSum:
						largestSum = temp_sum
						largestSubmatrix = subMatrix
	return(largestSum, largestSubmatrix)


# Return sub matrix
#   x, y are top left coordinates of the sub matrix with respect to the full matrix
#   w is the width of the sub matrix
#   h is the height of the sub matrix
def getSubMatrix(x, y, w, h, M):
	subMatrix = []
	for i in range(x, x+w):
		row = []
		for j in range(y, y+h):
			row.append(M[i][j])
		subMatrix.append(row)
	return subMatrix


def getSubMatrixZeros(x, y, w, h, M):
	N = len(M)
	subMatrix = []
	for i in range(0, N):
		row = []
		for j in range(0, N):
			if (i >= x and i < x+w) and (j >= y and j < j+h):
				row.append(M[i][j])
			else:
				row.append("_")
		subMatrix.append(row)
	return subMatrix


def sumMatrix(M):
	matrixSum = 0
	for row in M:
		for item in row:
			if isinstance(item, int):
				matrixSum += item
	return matrixSum


def printMatrix(M):
	for row in M:
		for item in row:
			if isinstance(item, int):
				print('{0:7d}'.format(item), end="")
			else:
				print('{0:7}'.format(""), end="")
		print()
	print()


def testMatrix(M):
	print("--------------- Test Case ---------------")
	(largestSum, largestSubmatrix) = getLargestSumMatrix(M)
	print("The full matrix is the following...")
	printMatrix(M)
	print("Below is the submatrix with the largest sum of", largestSum)
	printMatrix(largestSubmatrix)
	print()
	print()


# Test cases
M1 = [[1, 2], 
	[3, 4]]

M2 = [[-11, 0, 3], 
	[4, 5, 6], 
	[7, -8, 9]]

M3 = [[-1, 1, 1], 
	[-1, 11, 1], 
	[-1, 1, -3]]

# what do i return if there are sub matrixes with tied largest sum?
M4 = [[-1, 0, 0, 0, -1],
	[0, 0, 0, 0, 0],
	[0, 0, 22, 0, 0],
	[0, 0, 0, 0, 0],
	[-1, 0, 0, 0, -1]]

if __name__ == '__main__':
	testMatrix(M1)
	testMatrix(M2)
	testMatrix(M3)
	testMatrix(M4)
