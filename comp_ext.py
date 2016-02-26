#for dejeane only for now
def get_compatible_extention(word_i, word_j, i, j, morphisme_parts):
	prev_i = word_i[0]
	prev_j = word_j[0]
	i0 = i
	j0 = j
	comp_ext = ""
	#Right compatible extention
	while (word_i[i] == word_j[j] or word_j[j] == "*" or word_i[i] == "*"):
		comp_ext+=word_j[j]
		i, j = i+1, j+1
		if i>= len(word_i):
			if j>= len(word_j):
				raise Exception("SLOZHNAAAAA")#TODO actually
			else:
				word_i+=morphisme_parts[word_j[j]]
		if j>= len(word_j):
			if i>= len(word_i):
				raise Exception("SLOZHNAAAAA")#TODO actually
			else:
				word_j+=morphisme_parts[word_i[i]]
	i, j = i0, j0

	while (word_i[i] == word_j[j] or word_j[j] == "*" or word_i[i] == "*"):
		comp_ext = word_j[j] + comp_ext
		i, j = i-1, j-1
		if i<0:
			if j<0:
				raise Exception("SLOZHNAAAAA")#TODO actually
			else:
				word_i = morphisme_parts[word_j[j]]+word_i
				i+=len(morphisme_parts[word_j[j]])
		if j<0:
			if i<0:
				raise Exception("SLOZHNAAAAA")#TODO actually
			else:
				word_j = morphisme_parts[word_i[i]]+word_j
				j+=len(morphisme_parts[word_i[i]])

	return comp_ext, prev_i, prev_j
