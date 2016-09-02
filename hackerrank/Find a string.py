# og = input()
# sub = input()

og = "ABCDCDC"
sub = "CDC"

print(og, sub)



def numSubOccurance(og, sub):
	# assume len of sub >= 1
	occurances = 0

	for i in range(len(og)):

		# if first character matches sub, check whole sub
		if og[i] == sub[0]:

			match = False
			for j in range(len(sub)):
				if (i+j) < len(og) and og[i + j] == sub[j]:
					match = True
				else:
					match = False
					break;

			if match:
				occurances += 1
	return occurances

print(numSubOccurance(og, sub))