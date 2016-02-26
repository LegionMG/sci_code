


def get_funcs(_type):
	if _type == "arshon":
		return iter_arshon, jokerify_arshon, count_arshon
	elif _type == "thue":
		return iter_thue, jokerify_thue, count_thue
	elif _type == "leech":
		return iter_leech, jokerify_leech, count_leech

def iter_arshon(word):
	new_word = ""
	for i in range(len(word)):
		if i%2==1:
			if word[i]=='a':
				new_word+="cba"
			if word[i]=='b':
				new_word+="acb"
			if word[i]=='c':
				new_word+="bac"
		elif i%2==0:
			if word[i]=='a':
				new_word+="abc"
			if word[i]=='b':
				new_word+="bca"
			if word[i]=='c':
				new_word+="cab"
	return new_word

def iter_dejeane(word):
	new_word = ""
	for i in word:
		if i=="a":
			new_word+="abcacbcabcbacbcacba"
		if i=="b":
			new_word+="bcabacabcacbacabacb"
		if i=="c":
			new_word+="cabcbabcabacbabcbac"
	return new_word

def iter_thue(word):
	new_word = ""
	for i in word:
		if i=="1":
			new_word+="12312"
		if i=="2":
			new_word+="131232"
		if i=="3":
			new_word+="1323132"
	return new_word



def iter_leech(word):
	new_word = ""
	for i in word:
		if i=="0":
			new_word+="0121021201210"
		if i=="1":
			new_word+="1202102012021"
		if i=="2":
			new_word+="2010210120102"
	return new_word


def iter_11(word):
	new_word = ""
	for i in word:
		if i == "a":
			new_word+="12131232123"
		if i == "b":
			new_word+="13212321323"
		if i == "c":
			new_word+="13213121323"
	return new_word


def jokerify_arshon(word):
	new_word = ""
	for i in range(len(word)):
		if i%2==0:
			if word[i]=='a':
				new_word+="ab_"
			if word[i]=='b':
				new_word+="bca"
			if word[i]=='c':
				new_word+="cab"
		elif i%2==1:
			if word[i]=='a':
				new_word+="cba"
			if word[i]=='b':
				new_word+="acb"
			if word[i]=='c':
				new_word+="bac"
	return new_word

def jokerify_leech(word):
	new_word = ""
	for i in word:
		if i=="a":
			new_word+="abc_acb_a_cba"
		if i=="b":
			new_word+="bca_b_cab_acb"
		if i=="c":
			new_word+="cab_c_abc_bac"
	return new_word


def jokerify_thue(word):
	new_word = ""
	for i in word:
		if i=="a":
			new_word+="abс_b"
		if i=="b":
			new_word+="acabcb"
		if i=="c":
			new_word+="acbcacb"
	return new_word

def test_morphism(iter_func):
	nonquads = ["abaca", "abacb","abcab", "abc"]


def count_arshon(word):
	odd = {"a":0,"b":0,"c":0}
	even = {"a":0,"b":0,"c":0}
	for i in range(len(word)):
		if i%2==1:
			even[word[i]]+=1
		else:
			odd[word[i]]+=1
	print("even letters:", even)
	print("odd letters:", odd)

def count_leech(word):
	letters = {"0":0,"1":0,"2":0}
	for i in word:
		letters[i]+=1
	print(letters)

def count_dejeane(word):
	letters = {"a":0,"b":0,"c":0}
	for i in word:
		letters[i]+=1
	print(letters)

def count_thue(word):
	letters = {"1":0,"2":0,"3":0}
	for i in word:
		letters[i]+=1
	print(letters)

def get_words(length):
	queue = ["a","b","c"]
	while len(queue[0]) < length:
		word = queue.pop(0)
		queue.append(word+"a")
		queue.append(word+"b")
		queue.append(word+"c")
	return queue

"only small xx"
def filter_file():
	f = open("words.txt", "r+")
	f_ = open("nonquadras.txt","w+")
	for line in f:
		if "aa" in line:
			continue
		if "bb" in line:
			continue
		if "cc" in line:
			continue
		if "abab" in line:
			continue
		if "bcbc" in line:
			continue
		if "caca" in line:
			continue
		if "baba" in line:
			continue
		if "cbcb" in line:
			continue
		if "acac" in line:
			continue
		f_.write(line)
	f.close()
	f_.close()


def main():
	'''
	iterations = 2
	starting_word = word = "0"
	_type = "leech"
	iterate, jokerify, count = get_funcs(_type)
	for i in range(iterations):
		word = iterate(word)
		#print(jokerify(word))
		#print(i)
	f = open("word.txt", "w+")
	f.write(jokerify(word))
	f.close()
	words = get_words(5)
	f = open("words.txt", "w+")
	for word in words:
		f.write(word+"\n")
	f.close()
'''
	#f = open("nonquadras.txt", "r+")
	f = open("threes.txt", "r+")
	words = f.read().split()
	#print(words)
	for word in words:
		print(iter_dejeane(word), "\n---------")

if __name__ == "__main__":
	main()
