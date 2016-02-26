from quadra_filter import to_word, get_joker_positions

def string_to_codewalk(string):
	pass

def string_to_codeword(string):
	pass

def generate_codewords(length):
	q = ["0", "1"]
	cur_len = 1
	while(cur_len)<length:
		#print(q)
		cur_word = q.pop(0)
		cur_len = len(cur_word)
		if cur_len == length:
			break
		if cur_len >= 1 and cur_word[-1] == "0":
			#print(1)
			q.append(cur_word+"1")
		elif cur_len >= 3 and cur_word[-3:] != "111":
			#print(3)
			q.append(cur_word+"1")
			q.append(cur_word+"0")
		elif cur_len >= 3:
			#print(4)
			q.append(cur_word+"0")
		else:
			q+=[cur_word+"0", cur_word+"1"]
			
	return q


def get_fibonacchi_codewalk(number, depth):
	starts = [("2","1"),("3","1"),("3","2")]
	replace = dict()
	replace[starts[number][0]] = starts[number][0]+starts[number][1]
	replace[starts[number][1]] = starts[number][0]
	this_iter = starts[number][1]
	for i in range(depth):
		new_iter = "".join([replace[x] for x in this_iter])
		this_iter = new_iter
	return this_iter



def codewalk_to_string(codewalk):
	start = "aba"
	le = dict()
	le["ab"] = "c"
	le["ba"] = "c"
	le["ac"] = "b"
	le["ca"] = "b"
	le["bc"] = "a"
	le["cb"] = "a"
	for letter in codewalk:
		for i in range(int(letter)):
			start+=le[start[-2:]]
		start+=start[-2]
	return start


def check_codewalks(string):
	pass


def codeword_to_string(codeword):
	word = "ab"
	le = dict()
	le["ab"] = "c"
	le["ba"] = "c"
	le["ac"] = "b"
	le["ca"] = "b"
	le["bc"] = "a"
	le["cb"] = "a"
	for i in range(len(codeword)-1, -1, -1):
		if codeword[i] == "0":
			word = word[1]+word
		else:
			word = le[word[0]+word[1]]+word
	return word


def codeword_to_codewalk(codeword):
	pass


def generate_codewalks(length):
	pass


def main_trash():
	length = 40
	q = ["0", "1"]
	cur_len = 1
	ref = []
	max_dencity = 0
	number_of_words = 0
	while(cur_len)<length:
		#print(q)
		cur_word = q.pop(0)
		if cur_len != len(cur_word):
			print(str(cur_len)+" is finished! Max dencity = "+str(max_dencity/cur_len)+"\n")
			f = open("some_res.txt", "a+")
			f.write("Length = "+str(cur_len)+"; Max jokers = "+str(max_dencity)+"\n")
			f.close()
			cur_len = len(cur_word)
			max_dencity = 0
			number_of_words = 0
			f = open(str(cur_len)+".txt", "w")
			f.write(str(max_words))
			f.close()
			max_words = []
		if cur_len == length:
			break
		if cur_len >= 1 and cur_word[-1] == "0":
			#print(1)
			q.append(cur_word+"1")
			w = codeword_to_string(q[-1])
			word = to_word(get_joker_positions(w))
			count = word.count("-")
			if count == max_dencity:
				number_of_words+=1
				max_words.append(w)
			if count > max_dencity:
				max_dencity = count
				max_words = [w]
		elif cur_len >= 3 and cur_word[-3:] != "111":
			#print(3)
			q.append(cur_word+"1")
			w = codeword_to_string(q[-1])
			word = to_word(get_joker_positions(w))
			count = word.count("-")
			if count == max_dencity:
				number_of_words+=1	
				max_words.append(w)
			if count > max_dencity:
				max_dencity = count
				max_words = [w]	
			q.append(cur_word+"0")
			w = codeword_to_string(q[-1])
			word = to_word(get_joker_positions(w))
			count = word.count("-")
			if count == max_dencity:
				number_of_words+=1
				max_words.append(w)
			if count > max_dencity:
				max_dencity = count
				max_words = [w]
		elif cur_len >= 3:
			#print(4)
			q.append(cur_word+"0")
			w = codeword_to_string(q[-1])
			word = to_word(get_joker_positions(w))
			count = word.count("-")
			if count == max_dencity:
				number_of_words+=1
				max_words.append(w)
			if count > max_dencity:
				max_dencity = count
				max_words = [w]
		else:
			q+=[cur_word+"0", cur_word+"1"]
			w = codeword_to_string(q[-1])
			word = to_word(get_joker_positions(w))
			count = word.count("-")
			if count == max_dencity:
				number_of_words+=1
				max_words.append(w)
			if count > max_dencity:
				max_dencity = count
				max_words = [w]
			w = codeword_to_string(q[-2])
			word = to_word(get_joker_positions(w))
			count = word.count("-")
			if count == max_dencity:
				number_of_words+=1
				max_words.append(w)
			if count > max_dencity:
				max_dencity = count
				max_words = [w]