def stepStairs(numStairs):
	if (numStairs == 1):
		return 1
	elif (numStairs == 2):
		return 2
	elif (numStairs == 3):
		return 4
	elif (numStairs <= 0):
		return 0
	else:
		# everything higher than 3
		sum = stepStairs(numStairs - 1) + stepStairs(numStairs - 2) + stepStairs(numStairs - 3)
		return sum

if __name__ == "__main__":
	output = stepStairs(10)
	print(output)