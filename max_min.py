 # #take input how many number of value have to give in a list and find min and max value
num=int(input("Enter the number"))
mylist=input().split()
for i in range(num):
    mylist[i]=int(mylist[i])
a=min(mylist)
b=max(mylist)
print("Minimum no.",a)
print("Maximum no.",b)
#or
num=int(input("Enter the number"))
mylist=input().split()
for i in range(num):
    mylist[i]=int(mylist[i])
minEle=mylist[0]
maxEle=mylist[0]
for val in mylist:
    if val< minEle:
        minEle=val
    if val > maxEle:
        maxEle=val
print(minEle,maxEle)
