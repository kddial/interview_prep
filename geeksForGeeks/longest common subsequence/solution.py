


def solution(str1, str2):
	count = 0
	lcs = ""

	for i in str1:
		if i in str2:
			if i not in lcs:
				count += 1
				lcs += i

	return (count, lcs)


if __name__ == '__main__':
	str1 = "aabc"
	str2 = "abc"

	result = solution(str1, str2)
	print(result)


	X = "AGGTAB"
	Y = "GXTXAYB"
	result = solution(X, Y)
	print(result)