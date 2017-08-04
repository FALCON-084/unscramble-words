print(bin(0b1110 ^ 0b101))

a= '1110'
b= '101'
if(len(a) != len(b)):
    a = '0'*len(b) + a
    b = '0'*len(a) + b
temp =''
for i in range(len(a)):
    if ( int(a[i]) + int(b[i])== 1) :
        temp+='1'
    else :
        temp+='0'

num = int(temp,2)
print(bin(num))
