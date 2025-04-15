#take input how many number of value have to give in a list and add it
num=int(input("Enter the number"))
mylist=input().split()
sumoflist=0
for i in range(num):
    sumoflist += int(mylist[i])
print(sumoflist)
