def coins(n, combo):
	# negative n is impossible
	if n < 0:
		return 0

	elif n == 0:
		# a coin has matched previously
		return 1
	else:
		ways = 0

		# if n matches a coin, then we have one possible way
		# if n == 1 or n == 5 or n == 10 or n == 25:
		# 	print("n: ", n)
		# 	ways += 1

		# check remainder n values
		ways += coins(n-25, combo)
		ways += coins(n-10, combo)
		ways += coins(n-5, combo)
		ways += coins(n-1, combo)

		return ways

if __name__ == "__main__":
	n = 7
	combo = []
	result = coins(n, combo)
	print(result)