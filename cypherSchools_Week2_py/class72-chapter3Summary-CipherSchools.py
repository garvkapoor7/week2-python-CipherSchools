#if statement
name = "harshit"
if name == "harshit" or name=="Harshit":
    print("You are harshit")
elif name=="mohit" or name=="Mohit":
    print("you are mohit")
else:
    print("you are not harshit")

#while statement
i = 0
while i<10:
    print("hello world")
    i+=1
while i<10:
    print(i)
    i+=1

#for loop
for i in range(1,11,2):
    print(i)

#break keyword
for i in range(1,11):
    if i==5:
        break
    print(i)

#continue keyword
for i in range(1,11):
   if i==5: 
    continue
    print(i)

for i in "harshit":
    print(i)
