#ask user a number
#calculate sum of digits

#num=1256
#int(num[0]) ---1
#int(num[1]) ---2
#int(num[2]) ---5
#int(num[3]) ---6
#i---> 0 to 3

total =0
num = input("Enter a number: ")
for i in range(0, num+1):
    total +=num[i]
print(total)