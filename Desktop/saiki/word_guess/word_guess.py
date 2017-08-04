def ref_word(word):
    #get only alphabets from a string
    refined_word =''
    for i in range(len(word)):
        if word[i].isalpha() == True :
            refined_word += word[i]
    return refined_word 
def word_index(word):
    #returns sorted form of word
    temp = [x for x in word]
    temp = sorted(temp)
    temp = "".join(temp)
    return temp
def key_in_dict(dict,key):
    #returns true if dict has the given key
    for i in dict.keys():
        if (i == key):
            return True
    else : 
        return False
word_comb = []
def find_combinations (word,lenght):
    #find all combinations that are possible with the given word
    #in the 4th following line if i.e if n>x is written , we get words of min lenght x 
    n = len(word)
    if (n == lenght) :
        word_comb.append(word)
    if( n >3 ) :
        for i in range(n) :
            temp2 = list(word)
            temp2.remove(word[i])
            new_word = ''
            for j in temp2 :
                new_word += j
            word_comb.append(new_word)
            find_combinations(new_word,len(new_word))
        #print("all new words added")
def refine_word_comb (word_comb):
    #removes duplicates from word_comb
    #word_comb.remove('')
    word_comb_set = set(word_comb)
    temp =[]
    for i in word_comb_set:
        temp.append(word_index(i))
    word_comb_set = set(temp)
    temp =[]
    for i in word_comb_set:
        temp.append(i)
    word_comb = list(word_comb_set)
    return word_comb


#print(word_comb)
# exp = list("saiki")
# exp.remove('i')
# print(str(exp))

temp = raw_input('enter the letters:')
import json
with open('word_guess/data.json', 'r') as fp:
    data = json.load(fp)
print ("the words can be")
find_combinations(temp,len(temp))
possible_list =refine_word_comb(word_comb)
for word in possible_list :
    if(key_in_dict(data,word)) :
        print (data[word])
# else :
#     print ("sorry , there are no words with letters in",temp)






