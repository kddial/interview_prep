def wordsnumbers(n):
	# dictionary of unique digits
	num_dict = {}
	num_dict["one"] = 1
	num_dict["two"] = 2
	num_dict["three"] = 3
	num_dict["four"] = 4
	num_dict["five"] = 5
	num_dict["six"] = 6
	num_dict["seven"] = 7
	num_dict["eight"] = 8
	num_dict["nine"] = 9
	num_dict["ten"] = 10
	num_dict["eleven"] = 11
	num_dict["twele"] = 12
	num_dict["thirteen"] = 13
	num_dict["fourteen"] = 14
	num_dict["fifthteen"] = 15
	num_dict["sixteen"] = 16
	num_dict["seventeen"] = 17
	num_dict["eighteen"] = 18
	num_dict["nineteen"] = 19
	num_dict["twenty"] = 20
	num_dict["thirty"] = 30
	num_dict["fourty"] = 40
	num_dict["fifty"] = 50
	num_dict["sixty"] = 60
	num_dict["seventy"] = 70
	num_dict["eighty"] = 80
	num_dict["ninety"] = 90

	num_dict_mult = {}
	num_dict_mult["hundred"] = 100
	num_dict_mult["thousand"] = 1000

	# split into words
	n = n.split(" ")

	# converted to integer
	converted = 0

	# find ints of 100s and 1000s
	for key in num_dict_mult.keys():
		if key in n:
			key_index = n.index(key)
			converted += (num_dict[n[(key_index - 1)]] * num_dict_mult[key])
			n[key_index] = "null"
			n[key_index - 1] = "null"

	# find unique numbers
	for key in num_dict.keys():
		if key in n:
			converted += num_dict[n[n.index(key)]]

	return converted

if __name__ == '__main__':
	text = "one hundred twenty five"
	print(wordsnumbers(text))