import math

# Checks if a word is a palindrome
def is_palindrome(word):
	for i in range(math.floor(len(word)/2)):
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
	return math.floor(len(word)/2)

# Return the minimum number of inserts to make word into a palindrome.
def find_min_inserts_palindrome(word):

	# return 0 for empty strings and single character words
	if len(word) <= 1:
		return 0

	# new word that will become a palindrome
	new_word = word
	insert_count = 0
	stop = 0

	# find largest palindrome
	# tuple = (index, palindrome length, palindrome word)
	largest = find_largest_palindrome(new_word)

	# loop until the whole world is a palindrome
	while (largest[2] != new_word):
		if stop >= 50:
			return "INFINITE LOOP, YOUR CODE IS MESSEDUP STahpP"
		stop += 1

		# Grab left character of palindrome
		if largest[0] >= 1:
			left_char = new_word[largest[0] - 1]
			right_part_index = largest[0]+largest[1]

			# if left char does not belong to the right side of palindrome, 
			# then insert char to the right of the palindrome
			# else, re-find largest palindrome because it may have updated from previous iteration
			right_partition = new_word[right_part_index:]

			if left_char not in right_partition:
				# insert to the right
				new_word = new_word[:right_part_index] + left_char + new_word[right_part_index:]
				# update largest palindrome
				largest = (largest[0] - 1, largest[1] + 2, left_char + largest[2] + left_char)
				insert_count += 1
			else:
				# re-find largest palindrome
				largest = find_largest_palindrome(new_word)
				print("---------------1", new_word, largest)

		# Grab right character of palindrome
		right_part_index = largest[0]+largest[1]
		if right_part_index < len(new_word):

			# insert right character to the left side of palindrome
			right_char = new_word[right_part_index]
			new_word = new_word[:largest[0]] + right_char + new_word[largest[0]:]

			# update largest palindrome
			largest = (largest[0], largest[1] + 2, right_char + largest[2] + right_char)
			insert_count += 1

	print("Word:", word, "\tNew:", new_word, "\tCount:", insert_count)
	return insert_count



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

	print(find_min_inserts_palindrome("a"))
	find_min_inserts_palindrome("ab")
	find_min_inserts_palindrome("abc")
	find_min_inserts_palindrome("abcd")
	find_min_inserts_palindrome("aba")
	find_min_inserts_palindrome("geeks")
	find_min_inserts_palindrome("sgeeks") # == 2
	find_min_inserts_palindrome("abcddae") # == 3 WRONG ATM
	find_min_inserts_palindrome("abcab") # == 2

