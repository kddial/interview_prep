# http://www.practice.geeksforgeeks.org/problem-page.php?pid=557

# Checks if a word is a palindrome
def is_palindrome(word):
	for i in range(int(len(word)/2)):
		if word[i] != word[len(word) - 1 - i]:
			return False
	return True


# Returns largest palindrome as a tuple 
# or returns None if palindrome does not exist.
# tuple: (index, length of palindrome, palidrome word)
#
# Note: single character words are not palindrome for this function 
def find_largest_palindrome(word):
	# do not account for single character words
	if len(word) <= 1:
		return None

	# create windows that decrements in size
	for window in range(len(word), 1, -1):

		# move the window from left index to right
		for j in range(len(word) - window + 1):
			window_word = word[j:j+window]

			if (is_palindrome(window_word)):
				return (j, window, window_word)

	# when no palindrome is found, return the middle character as the palindrome
	middle_index = find_middle_character_index(word)
	return (middle_index, 1, word[middle_index])


# Return the index of the middle character of the word, which will be used as a starting palindrome
# if len(word) is even, return the character to the right of the middle index
def find_middle_character_index(word):
	return int(len(word)/2)

# Return the minimum number of inserts to make word into a palindrome.
def find_min_inserts_palindrome(word):

	# return 0 for empty strings and single character words
	if len(word) <= 1:
		return 0

	# new word that will become a palindrome
	new_word = word
	insert_count = 0
	stop = 0
	in_right_partition = False
	in_left_partition = False

	# find largest palindrome
	# tuple = (index, palindrome length, palindrome word)
	largest = find_largest_palindrome(new_word)

	# loop until the whole world is a palindrome
	while (largest[2] != new_word):
		if stop >= 50:
			print("INFINITE LOOP, YOUR CODE IS MESSEDUP STahpP")
			return -1
		stop += 1

		# Grab left character of palindrome
		if largest[0] >= 1:

			# if left char does not belong to the right side of palindrome, 
			# then insert char to the right of the palindrome
			# else, re-find largest palindrome because it may have updated from previous iteration
			left_char = new_word[largest[0] - 1]
			right_part_index = largest[0]+largest[1]
			right_partition = new_word[right_part_index:]


			# Extreme edge case left char and right char are in the opposing paritions.
			# So just choose left char to be inserted.
			if (left_char not in right_partition) or (in_right_partition and in_left_partition):
				# insert left char to the right side of palindrome, update largest palindrome
				new_word = new_word[:right_part_index] + left_char + new_word[right_part_index:]
				largest = (largest[0] - 1, largest[1] + 2, left_char + largest[2] + left_char)
				insert_count += 1
			else:
				# re-find largest palindrome
				in_right_partition = True
				largest = find_largest_palindrome(new_word)

		# Grab right character of palindrome
		right_part_index = largest[0]+largest[1]
		if right_part_index < len(new_word):


			# if right char does not belong to the left side of palindrome, 
			# then insert char to the left of the palindrome
			# else, re-find largest palindrome because it may have updated from previous iteration
			right_char = new_word[right_part_index]
			left_partition = new_word[:largest[0]]

			if right_char not in left_partition:
				# insert right char to the left side of palindrome, update largest palindrome
				new_word = new_word[:largest[0]] + right_char + new_word[largest[0]:]
				largest = (largest[0], largest[1] + 2, right_char + largest[2] + right_char)
				insert_count += 1
			else:
				# re-find largest palindrome
				in_left_partition = True
				largest = find_largest_palindrome(new_word)

	# print("Word:", word, "\tNew:", new_word, "\tCount:", insert_count)
	return insert_count

def geeksForGeeksWrapper(solution_function):
	# Input number of test cases
	t = int(raw_input())
 
	# One by one run for all input test cases
	for i in range(0,t):

		# grab raw test case
		test_case = raw_input()

		# run solution function on test case
		print(solution_function(test_case))


if __name__ == "__main__":
	# test helper functions
	assert is_palindrome("aba") == True
	assert is_palindrome("abaa") == False
	assert is_palindrome("") == True
	assert is_palindrome("a") == True
	assert is_palindrome("aaaa") == True
	assert is_palindrome("abcd") == False
	assert is_palindrome("baab") == True
	assert is_palindrome("ebaade") == False
	assert is_palindrome("ebaabe") == True

	assert(find_largest_palindrome("baa") == (1, 2, "aa"))
	assert(find_largest_palindrome("baab") == (0, 4, "baab"))
	assert(find_largest_palindrome("aa") == (0, 2, "aa"))
	assert(find_largest_palindrome("aab") == (0, 2, "aa"))
	assert(find_largest_palindrome("") == None)
	assert(find_largest_palindrome("a") == None)
	assert(find_largest_palindrome("ab") == (1, 1, "b"))
	assert(find_largest_palindrome("abc") == (1, 1, "b"))

	# test real function
	assert(find_min_inserts_palindrome("a") == 0)
	assert(find_min_inserts_palindrome("ab") == 1)
	assert(find_min_inserts_palindrome("abc") == 2)
	assert(find_min_inserts_palindrome("abcd") == 3)
	assert(find_min_inserts_palindrome("aba") == 0)
	assert(find_min_inserts_palindrome("geeks") == 3)
	assert(find_min_inserts_palindrome("sgeeks") == 2)
	assert(find_min_inserts_palindrome("abcddae") == 3)
	assert(find_min_inserts_palindrome("abcab") == 2)

geeksForGeeksWrapper(find_min_inserts_palindrome)
