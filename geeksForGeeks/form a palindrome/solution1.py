
def find_num_of_min_inserts(word):

	if len(word) <= 1:
		return 0
	else:
		if word[0] == word[-1]:
			return find_num_of_min_inserts(word[1:-1])
		else:
			# insert to match first char
			first = find_num_of_min_inserts(word[1:]) + 1

			# insert to match last char
			last = find_num_of_min_inserts(word[:-1]) + 1

			return min(first, last)


if __name__ == '__main__':

	# # test real function
	assert(find_num_of_min_inserts("a") == 0)
	assert(find_num_of_min_inserts("ab") == 1)
	assert(find_num_of_min_inserts("abc") == 2)
	assert(find_num_of_min_inserts("abcd") == 3)
	assert(find_num_of_min_inserts("aba") == 0)
	assert(find_num_of_min_inserts("geeks") == 3)
	assert(find_num_of_min_inserts("sgeeks") == 2)
	assert(find_num_of_min_inserts("abcddae") == 3)
	assert(find_num_of_min_inserts("abcab") == 2)