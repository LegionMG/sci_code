def get_joker_positions(word):
    positions = [0 for i in word]
    queue = [""]
    prev_q = [""]
    most_right_subword_end = [{} for i in range(len(word)+1)]
    for i in range(len(word)):
        new_q = [subword+word[i] for subword in queue if len(subword) < 7]
        for subword in new_q:
            if subword in most_right_subword_end[len(subword)]:
                if most_right_subword_end[len(subword)][subword] == i-len(subword)-1:
                    try:
                        positions[i+1] = 1
                    except:
                        pass
                    try:
                        positions[most_right_subword_end[len(subword)][subword]+1] = 1
                    except:
                        pass
                    try:
                        if most_right_subword_end[len(subword)][subword]-len(subword) >= 0:
                                positions[most_right_subword_end[len(subword)][subword]-len(subword)] = 1
                    except:
                        pass
            most_right_subword_end[len(subword)][subword] = i
        new_q += [""]
        queue, new_q, prev_q = new_q, [], queue
    #print('MOST LENG', max([len(x) for x in most_right_subword_end]))
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
	   #for i in range(3):
        #f = open("ans.txt", "a+")
        for iteration in range(0, 33):
            print("Fibonacci word #"+str(2)+". Iteration #"+str(iteration)+"\n")
            cwk = get_fibonacci_codewalk(2, iteration)
            word = codewalk_to_string(cwk)
            mask = get_joker_positions(word)
            print(len(mask))
            #print(mask)
            count = mask.count(0)
            print("Dencity = "+str(count/len(word))+"\n")
        #f.close()


if __name__ == '__main__':
	main()