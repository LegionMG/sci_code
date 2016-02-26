from random import choice, random
from time import time



def get_random_letter(last_letter):
	a = random()*19
	if a < 3/19:
		return "*"
	elif a< 8.33333/19:
		return "a"
	elif a < 12.66666/19:
		return "b"
	return "c"


def get_random_letter2(last_letter):
	alphabet = ["a","b","c","a","b","c","a","b","c","*","*"]
	a = choice(alphabet)
	while a == last_letter:
		a = choice(alphabet)
	return a


def compare(u, w):
	if len(w) > len(u):
		return False
	if len(w) == 1 and (w == "*" or u[len(u)-1] == "*"):
		return False
	if u == w:
		return True
	for i in range(len(w)-1, -1, -1):
		if w[i] == u[len(u)-len(w)+i] or w[i] == "*" or u[len(u)-len(w)+i] == "*":
			continue
		else:
			return False
	return True

stringa = "bc*bac*bcacb*cabacbca*cba*cabac*abc*acbcabac*bcacb*cab*cb"

def has_repetit(word):
	stub = ""
	for i in word:
		stub+=i
		if seek_and_del_repetition(stub)!= stub:
			print(seek_and_del_repetition(stub), stub)
			return True
	return False

def seek_and_del_repetition(word):
	for i in range(len(word)-1,-1, -1):
		if compare(word[:i], word[i:]):
			#print(word[:i], word[i:], word)
			return word[:i]
	return word


def main():
	kek = time()
	word = ""
	last_letter = ""
	length = 100
	#print(compare("*c*", "aca"))

	'''
	for i in range(steps):
		last_letter = get_random_letter(last_letter)
		word+= last_letter
		word = seek_and_del_repetition(word)
		print("{0} iteration: ".format(i)+word+"\n tried to add:"+last_letter)
	'''
	l = 0
	while len(word) < length:
		last_letter = get_random_letter(last_letter)
		word+= last_letter
		word = seek_and_del_repetition(word)
		# if len(word)>l:
		# 	print(len(word))
		# 	l = len(word)
		#if length%len(word) == 0:
		#	print("{0} iteration: ".format(len(word))+word+"\n tried to add:"+last_letter)

	print(word)
	print("Time spent :" + str(time() - kek))
	print("Density of holes : "+ str(word.count("*")/len(word)))

if __name__ == "__main__":
	main()
