from time import time
from quadra_filter import to_word
from random import choice
from gen_quadra import get_random_letter2, remove_repetition, has_repetit
from arshon_stab import iter_thue, iter_leech, iter_dejeane, iter_arshon


def get_joker_positions(word):
    positions = [0] * len(word)
    queue = [""]
    prev_q = [""]
    most_right_subword_end = dict()  # [{} for i in range(len(word)+1)]

    for i in range(len(word)):
        new_q = [subword+word[i] for subword in queue if len(subword) < subword_len_petrova[CASE]]
        for subword in new_q:
            idx = most_right_subword_end.get(subword)
            if idx == i - len(subword) - 1:
                try:
                    positions[i + 1] = 1
                except:
                    pass

                positions[idx + 1] = 1

                if 0 <= idx - len(subword) < len(positions):
                    positions[idx - len(subword)] = 1
            
            most_right_subword_end[subword] = i
        new_q += [""]
        queue, new_q, prev_q = new_q, [], queue
    #print('MOST LENG', max([len(x) for x in most_right_subword_end]))
    return positions

def apply_mask(word, mask):
    return ''.join(["*" if mask[i]==0 else word[i] for i in range(len(word))])

def string_to_codeword(word):
    return "".join(["0" if word[i]==word[i+2] else "1" for i in range(len(word)-2)])

def string_to_codewalk(word):
    c = 0
    res = ""
    word = string_to_codeword(word)
    s = 0
    while word[s]!="0":
        s+=1
    for i in range(s+1, len(word)):
        if word[i] == "1":
            c+=1
        else:
            res+=str(c)
            c = 0
    return res

def clean_dict(dic, i):
    all_keys = list(dic.keys())
    for key in all_keys:
        if dic[key] < i-len(key)-1:
            dic.pop(key)
    return dic


def get_fibonacci_codewalk(depth):
    starts = [("2","1"),("3","1"),("3","2")]
    replace = dict()
    replace[starts[CASE][0]] = starts[CASE][0]+starts[CASE][1]
    replace[starts[CASE][1]] = starts[CASE][0]
    this_iter = starts[CASE][1]
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
            start += next_let[start[-2:]]
        start += start[-2]
    return start


def beta(word):
	return "".join(["fgf" if letter == "f" else "fgg" for letter in word])

subword_len_petrova = [5, 3, 7]
CASE = 1

def main():
       #for i in range(3):
        #f = open("ans.txt", "a+")
    for iteration in range(33, 50):
        t1 = time()
        print("Fibonacci word #" + str(CASE) + ". Iteration #" + str(iteration) + "\n")
        cwk = get_fibonacci_codewalk(iteration)
        word = codewalk_to_string(cwk)
        mask = get_joker_positions(word)
        print(len(mask))
        #print(mask)
        count = mask.count(0)
        print("Dencity = "+str(count/len(word))+"\n")
        print("Time: {} sec".format(time() - t1))
        #f.close()

def main2():
	start = "f"
	for cwk in ["132123132","132123123","132132123132","123132123123","132132123132132","123132123132132", "132132123123132", "123132123123132", "132132123123132123123132"]:
		print(cwk)
		print(codewalk_to_string(cwk))
		print(to_word(get_joker_positions(codewalk_to_string(cwk))))

def get_random_letter2(last_letter):
    alphabet = ["a","b","c"]
    a = choice(alphabet)
    #print(a)
    while a == last_letter:
        a = choice(alphabet)
    return a

def main3():
    length = 40

    word = "*"
    count = 9
    wheels = 10
    cur_max_len = 0
    while cur_max_len< length:
        print(word)
        if count >0 or has_repetit(word+"*"):
            if wheels <= 0:
                pass
            a = get_random_letter2(word[-1])
            while has_repetit(word+a):
                a = get_random_letter2(word[-1])
            word+=a
            count -= 1
        elif count <= 0:
            if has_repetit(word+"*"):
                word = remove_repetition(word+"*")
                wheels -= 1
            word+="*"
            count = 9

        cur = len(word)
        if cur> cur_max_len:
            cur_max_len = cur
            print(cur_max_len)

def main5():
    for word in ["abc", "acb", "bca", "bac", "cab","cba"]:
        print(iter_arshon(word))
        print(to_word(get_joker_positions(iter_arshon(word))))

def main4():
    cwk = "1"
    steps = 4
    for _ in range(steps):
        t1 = time()
        cwk = iter_dejeane(cwk)
        word = codewalk_to_string(cwk)
        mask = get_joker_positions(word)
        print(len(mask))
        #print(mask)
        holed = apply_mask(word, mask)
        print(has_repetit(holed))
        count = mask.count(0)
        print("Dencity = "+str(count/len(word))+"\n")
        print("Time: {} sec".format(time() - t1))
        #f.close()

def main6():
    f = open("results.txt","r")
    s = f.read().split()
    f.close()
    f = open("new.txt", "w")
    for word in s:
        w = codewalk_to_string(word)
        mask = get_joker_positions(w)
        if not has_repetit(apply_mask(w, mask)):
            f.write(word+"\n")
    f.close()



if __name__ == '__main__':
    #print(has_repetit("abacabcbacbcacbacabcbacbcabacbabcacbacabcbacbcabacbabcbacbcaba"))
    main6()
