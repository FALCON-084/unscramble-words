file1 = open('88_narcisticNumbers.txt','r+')
file2 = open('output.txt','w')
temp = file1.readline()

def split_pow(number,power):
    '''tests if the split power of number to the power power is equal to that number or not '''
    num_back = number
    temp =0
    while(number>0):
        temp += (number % 10)**power 
        number/=10
    #return temp
    if(num_back==temp):
        return True
    else :
        return False
def ret_index(pp_num):
    '''returns the index for plusperect numbers'''
    for i in range(50):
        if(split_pow(pp_num,i)==True):
            return i

while(temp !=''):
    file2.write("%s :- index %d \n" %(temp,ret_index(int(temp))))
    temp =file1.readline()