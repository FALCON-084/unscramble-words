#n = int(input("enter the number of digits in your number:"))

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

def print_limits_low (power):
    return len(str(9**power))

'''
for j in range(2,9):
    check_upto = 10**print_limits_low(j)
    for i in range (2,check_upto):
        if(split_pow(i,j) == True):
            print("%d under power %d \n" %(i,j))
'''
print 4**5 + 1 + 0 + 5**5