def get_codeword(word):
	result = ""
	for i in range(len(word)-2):
		if word[i] == word[i+2]:
			result+="1"
		else:
			result+="0"
	return result

def get_codewalk(codeword):
	i = 0
	while codeword[i] == "0":
		i+=1
	result = ""
	count = 0
	for j in range(i, len(codeword)):
		if codeword[j] == "0":
			count+=1
		else:
			result+=str(count)
			count = 0
	return result[1:]