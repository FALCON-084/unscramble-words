line = raw_input("what line do you want:")
n = int(raw_input("how many:"))

for i in range(2,n+1):
    temp =""
    for j in range (0,len(line)):
        if(line[j] == '1'):
            temp += str(i)
        else :
            temp+= str(line[j])
    print temp

