import queue
from ite2 import codewalk_to_string, string_to_codewalk, has_repetit
class Cwk_automata:
	def __init__(self):
		self.state = 0
		self.table = {
			0:{
				"1": 1,
				"2": 2,
				"3": 3
			},
			1:{
				"2": 2,
				"3": 3
			},
			2:{
				"1": 1,
				"2": 4,
				"3": 3
			},
			3:{
				"1": 1,
				"2": 5,
				"3": 6
			},
			4:{
				"1": 1,
			},
			5:{
				"1": 1,
				"3": 3
			},
			6:{
				"1": 1,
				"2": 5
			}
		}
	def set_state(self, state):
		self.state = state

	def get_state(self):
		return self.state

	def get_state_data(self):
		return list(self.table[self.state].keys())

	def step(self, letter):
		if letter in self.get_state_data():
			self.state =  self.table[self.state][letter] 
		else:
			return False
		return self.state

	def read_word(self, word):
		self.set_state(0)
		print(word)
		i = 0
		for letter in word:
			#print(letter)
			if self.step(letter):
				#print(self.get_state())
				pass
			else:
				break
		else:
			return True
		return False

def refine_word(word):
	mask = [1]*(len(word)+1)
	pairs = []
	for i in range(len(word)):
		if i>1:
			if word[i] == "2":
				pairs.append((i-1, i))
			w = word[i-1:i+1]
			if w=="12" or w=="21" or w=="22" or w=="33":
				mask[i] = 0
			if w=="13":
				mask[i+1] = 0
			if w=="31":
				mask[i-1] = 0
			if w=="33":
				pairs.append((i-1, i+1))
		if i>=3:
			w = word[i-3:i+1]
			if w == "1221" or w=="2332":
				mask[i+1] = 0
				mask[i-3] = 0
		if i>=7:
			w = word[i-7:i+1]
			if w == "12123213" or w == "12313232":
				mask[i-7] = 0
				mask[i-3] = 0
			if w == "31232121" or w == "23231321":
				mask[i+1] = 0
				mask[i-3] = 0
			if w == "13132312" or w == "21323131":
				mask[i-7] = 0
				mask[i+1] = 0
	for pair in pairs:
		if mask[pair[0]] == mask[pair[1]] == 1:
			mask[pair[1]] = 0
	mask[0] = 0
	return mask

def test():
	a = Cwk_automata()
	print(a.read_word("31232121"))
	print(a.read_word("11"))

def queue_get_all(q):
    items = []
    maxItemsToRetreive = 10000000000000
    for numOfItemsRetrieved in range(0, maxItemsToRetreive):
        try:
            if numOfItemsRetrieved == maxItemsToRetreive:
                break
            items.append(q.get_nowait())
        except:
            break
    return items

def get_words(length):
	q = queue.Queue()
	aut = Cwk_automata()
	q.put(("", 0))
	cur_len = 0
	while cur_len < length:
		word, state = q.get()
		if len(word) > cur_len:
			cur_len = len(word)
			print(cur_len)
		if cur_len == length:
			q.put((word, state))
			break
		else:
			aut.set_state(state)
			next_lets = sorted(aut.get_state_data())
			for let in next_lets:
				if check(word+let):
					aut.set_state(state)
					q.put((word+let, aut.step(let)))
	return sorted([x[0] for x in queue_get_all(q)])

def main1():
	length = 25
	aut = Cwk_automata()
	f = open("res1.txt", "w")
	f.close()
	dfs(aut, length, "", 0)



def dfs(aut, length, word, state):
	if len(word) >= length and check(word):
		su = sum(refine_word(word))/(len(codewalk_to_string(word))-3)
		if su >=(0.15):
			f = open("res1.txt", "a")
			f.write(word+" "+str(su)+"\n")
			f.close()
			return
	next_lets = sorted(aut.get_state_data())
	for letter in next_lets:
		aut.set_state(state)
		new_w = word+letter
		#print(len(new_w))
		if len(new_w)<=length:
			dfs(aut, length, new_w, aut.step(letter))

def check(word):
	anti = ["121312","131213","1232122","1323132","1323133","213121","232123","2212321","2313231","312131","321232","3231323","3313231", "132323232323", "33232323232","32323232323","232323232321","232323232323","123232323232"]
	for w in anti:
		if w in word:
			return False
	return True

def main():
	w = get_words(18)
	print(len(w))
	#m = [((sum(refine_word(x))/(len(codewalk_to_string(x))-3), x) for x in  w]
	k = [x for x in m if x[0]>(1/6)]
	#print(len(m))
	print(max(m))
	print(len(k))
	print(k)
	f = open("results.txt", "w")
	for x in k:
		f.write(x[1]+"\n")
	f.close() 
	#print(m)

def sus():
	f = open("results.txt", "r")
	s = f.read().split()
	f.close()
	z = open("new.txt", "w")
	for word in s:
		if check(word) and has_repetit(codewalk_to_string(word)):
			#z.write(word+" "+str(10/len(codewalk_to_string(word)))+"\n")
			z.write(word+"\n")
	z.close()

if __name__ == '__main__':
	print(sum(refine_word("12323231331323232323")),refine_word("12323231331323232323"), codewalk_to_string("12323231331323232323"), len(codewalk_to_string("12313232323231321323")))
	print(has_repetit(codewalk_to_string("12323231331323232323")))
	#print(check("123132323232323132"))
	#print(string_to_codewalk("cacbcabacbabcacbacabcbacbcabacbabcacbacabcb"))
	#print("123132313231323132")
	main1()
	#sus()
	#main()