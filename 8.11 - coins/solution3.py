
# anser without duplication
# ordering of coins does NOT matter


def coins(n):
	combos = {}
	combos[0] = [[]]
	combos[1] = [[1]]



	for i in range(2, n+1):
		combos[i] = []
		# every i has one possible way (1, 1, 1, 1, 1, ...)
		all_ones = [1] * i
		combos[i].append(all_ones)

		if i >= 5:
			for arr in combos[i-5]:
				arr2 = arr[:]
				arr2.append(5)
				arr2.sort()
				if arr2 not in combos[i]:
					combos[i].append(arr2)
				

		if i >= 10:
			for arr in combos[i-10]:
				arr2 = arr[:]
				arr2.append(10)
				arr2.sort()
				if arr2 not in combos[i]:
					combos[i].append(arr2)

		if i >= 25:
			for arr in combos[i-25]:
				arr2 = arr[:]
				arr2.append(25)
				arr2.sort()
				if arr2 not in combos[i]:
					combos[i].append(arr2)


	return combos



if __name__ == "__main__":
	n = 25
	combos = coins(n)

	for key in combos:
		print("{}: total= {}, combos={}".format(key, len(combos[key]), combos[key]))
		print()
