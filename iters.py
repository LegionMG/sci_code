def get_joker_positions(word):
	positions = [0 for i in word]
	queue = [""]
	prev_q = [""]
	most_right_subword_end = dict()
	for i in range(len(word)):
		print(i/len(word))
		#new_q = [subword+word[i] for subword in queue]
		for subword in queue:
			if subword+word[i] in most_right_subword_end and most_right_subword_end[subword+word[i]] == i-len(subword+word[i])-1:
				try:
					positions[i+1] = 1
				except:
					pass
				try:
					positions[most_right_subword_end[subword+word[i]]+1] = 1
				except:
					pass
				try:
					if most_right_subword_end[subword+word[i]]-len(subword+word[i]) >= 0:
						positions[most_right_subword_end[subword+word[i]]-len(subword+word[i])] = 1
				except:
					pass
			most_right_subword_end[subword+word[i]] = i
		most_right_subword_end = clean_dict(most_right_subword_end, i)
		queue, new_q, prev_q = [subword+word[i] for subword in queue]+[""], [], queue
	return(positions)

def clean_dict(dic, i):
	all_keys = list(dic.keys())
	for key in all_keys:
		if dic[key] < i-len(key)-1:
			dic.pop(key)
	return dic


def get_fibonacci_codewalk(number, depth):
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
	next_let = dict()
	next_let["ab"] = "c"
	next_let["ba"] = "c"
	next_let["ac"] = "b"
	next_let["ca"] = "b"
	next_let["bc"] = "a"
	next_let["cb"] = "a"
	for letter in codewalk:
		for i in range(int(letter)):
			start+=next_let[start[-2:]]
		start+=start[-2]
	return start

def main():
	for i in range(3):
		for iteration in range(15, 16):
			print("Fibonacci word #"+str(i)+". Iteration #"+str(iteration))
			cwk = get_fibonacci_codewalk(i, iteration)
			word = codewalk_to_string(cwk)
			count = get_joker_positions(word).count(0)
			print("Dencity = "+str(count/len(word)))


if __name__ == '__main__':
	main()