from time import time


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


if __name__ == '__main__':
    main()
