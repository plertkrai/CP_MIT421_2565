"""
Name: Puriwat Lertkrai
ID: 1111111111111
Group: MIT421
"""

# list
mylist = [10,20,30,40,50]
# add member to list
# append()
print(mylist)
# add 60 to mylist
mylist.append(60)
print(mylist)

mylist2 = [100,200,300]

mylist.extend(mylist2)
print(mylist)

mylist = mylist + mylist2
print(mylist)

# insert member to list
# insert(index,data)
mylist.insert(-3,400)
print(mylist)
# add 1000 to first member
mylist.insert(0,1000)
print(mylist)

# delete member in list
# remove()
mylist.remove(100)
print(mylist)

if 500 in mylist:
    mylist.remove(500)
else:
    print("list has no 500.")
print(mylist)

# pop
# del last member
mylist.pop()
print(mylist)
# del first member
mylist.pop(0)
print(mylist)

# del
# del first member
del mylist[0]
print(mylist)

#del mylist2
print(mylist2)

# change data in list
mylist[-1] = 2000
print(mylist)

mylist[0] = mylist[0]*100
print(mylist)

# sorting data in list
mylist2 = mylist
# sort()
mylist.sort() # low - high
print(mylist)

mylist.sort(reverse=True) #high - low
print(mylist)

# reverse()
print(mylist2)

# copy
newlist = mylist.copy()

mylist.append("MIT421")
print(mylist)

print(newlist)


