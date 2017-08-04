def ref_word(word):
    refined_word =''
    for i in range(len(word)):
        if word[i].isalpha() == True :
            refined_word += word[i]
    return refined_word 
def word_index(word):
    temp = [x for x in word]
    temp = sorted(temp)
    temp = "".join(temp)
    return temp
def key_in_dict(dict,key):
    for i in dict.keys():
        if (i == key):
            return True
    else : 
        return False
temp = raw_input('enter the letters:')
from itertools import permutations
perms = [''.join(p) for p in permutations(temp)]

#print(perms)
words = open("word_guess/words_3000.txt",'r')
word = words.readline()
word_list =[] 
while(word != ''):
    word_list.append(ref_word(word))
    word = words.readline()
#print(word_list)
numb =0
word_dict = {}
for word in word_list:
    idx = word_index(word)
    print(numb)
    if(key_in_dict(word_dict,idx)) :
        word_dict[idx].append(word)
    else :
        word_dict[idx] = [word]
    numb+=1

import json
with open('word_guess/data_3000.json', 'w') as fp:
    json.dump(word_dict, fp, sort_keys=True,indent=0)
#print(word_list)
'''
for i in perms :
    for j in word_list :
        if(i==j): 
            new.write("%s\n" %(i))

'''




