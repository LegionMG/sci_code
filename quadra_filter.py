
#filter_file()
#
"-x-xxxx-x"
"abcacbabc"
"000001000"

'0 - ok; 1 - not ok'
def get_joker_positions(word):
	positions = [0 for i in word]
	queue = [""]
	prev_q = [""]
	most_right_subword_end = dict()
	for i in range(len(word)):
		new_q = [subword+word[i] for subword in queue]
		for subword in new_q:

			if subword in most_right_subword_end.keys() and most_right_subword_end[subword] == i-len(subword)-1:

				#print(subword)
				try:
					positions[i+1] = 1
				except:
					pass
				#print(most_right_subword_end[subword])
				try:
					positions[most_right_subword_end[subword]+1] = 1
				except:
					pass
				try:
					if most_right_subword_end[subword]-len(subword) >= 0:
						positions[most_right_subword_end[subword]-len(subword)] = 1
					#print(subword, i+1, most_right_subword_end(subword)+1, most_right_subword_end(subword)-len(subword))
				except:
					pass
			most_right_subword_end[subword] = i

		new_q += [""]
		#print(prev_q, new_q)
		#print(positions, i)
		queue, new_q, prev_q = new_q, [], queue
	return(positions)

def to_word(array):
	string = ""
	for i in array:
		if i == 1:
			string+="x"
		else:
			string+="-"
	return string

def main():
	f = open("dej_threes.txt", "r+")
	words = f.read().split()
	for word in words:
		result = get_joker_positions(word)
		print(word)
		print(to_word(result))


if __name__ == "__main__":
	main()