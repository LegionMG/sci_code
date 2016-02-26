import quadra_filter as q
def main():
	word = "abc"
	steps = 1
	dic = dict()
	dic["a"] = "abcacbcabcbacbcacba"
	dic["b"] = "bcabacabcacbacabacb"
	dic["c"] = "cabcbabcabacbabcbac"
	i = 0
	while i <= steps:
		print(i)
		i+=1
		word1 = str()
		for letter in word:
			word1+=dic[letter]
		word = word1[:]
	print(word)
	print(q.get_joker_positions(word).count(0)/len(word))


if __name__ == "__main__":
	main()