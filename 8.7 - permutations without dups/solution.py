# yass i beat chan :D. handicapped him at 4am.

def permNoDups(str):
	if len(str) == 1:
		return [str]

	else:
		perms = []

		for i in range(len(str)):
			char = str[i]
			str_wo_char = str[0:i] + str[i+1:len(str)]

			temp_perms = permNoDups(str_wo_char)

			# append char to perms
			for p in temp_perms:
				perms.append(char + p)
		return perms

result = permNoDups("abcd")
print(result)