
# solution where coin ordering matters
# so money 15 can have 7 total possible combinations:
# combos=[
# [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], 
# [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 5], 
# [1, 1, 1, 1, 1, 5, 5], 
# [5, 5, 5], 
# [10, 5],                 <-  duplicate
# [1, 1, 1, 1, 1, 10], 
# [5, 10]]                 <-  duplicate


def coins(n):
	ways = [0] * (n+1)
	ways[0] = 1 # one way if n equals a coin
	ways[1] = 1

	for i in range(2, n+1):
		# every i has one possible way (1, 1, 1, 1, 1, ...)
		nums = 1

		if i >= 5:
			nums += ways[i-5]

		if i >= 10:
			nums += ways[i-10]

		if i >= 25:
			nums += ways[i-25]

		ways[i] = nums

	return ways





if __name__ == "__main__":
	n = 15
	result = coins(n)
	print(result[n])