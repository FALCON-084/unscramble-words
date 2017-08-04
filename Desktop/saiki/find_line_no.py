fp = open("sample.jsonl",'r')
fp.seek(-100000,2)
#text = raw_input("enter the phrase to search for:")
#do =raw_input("enter r to go on or q to exit:")
line_no =0
'''
while(do == 'r'):
    for i in range (50000):
        line_no +=1
        temp = str(fp.readline())
        if(temp.find(text)>0) :
            print("found in line no :-",line_no)
            print(temp)
    do =raw_input("enter r to go on or q to exit:")
    '''

temp = str(fp.readline())
fp2 = open ('refind...txt','w')
while(temp != ''):
    fp2.write(temp)
    temp = str(fp.readline())
fp2.close()
fp.close()
