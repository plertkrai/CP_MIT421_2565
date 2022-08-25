"""
Name: Puriwat Lertkrai
ID: 1111111111111
Group: MIT421
"""

# logical operators
x,y,z = 10,20,30
# and
print(x>y and y<z) # F and T --> F
print((x and (y==z)) and (y and (y==x)))
# or
print(x==10 or x==100) # T
# not
print(not(not(x==10 or x==100))) #T


print(not(not(x==10 or x==100)) and x!=y or y==z) #T