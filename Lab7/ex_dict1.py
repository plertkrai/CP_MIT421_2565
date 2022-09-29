"""
Name: Puriwat Lertkrai
ID: 1111111111111
Group: MIT421
"""


# Data collection - Dictionary
# keys:values

d = {"name":"Puriwat","age":36,"major":"MIT"}
print(type(d))
print(d)

# access to value in dictionary - using keys
print(d["name"])
print(d["age"])
print(d["major"])
#print(d["uni"])

# get()
print(d.get("name"))
print(d.get("age"))
print(d.get("major"))

# keys()
x = d.keys()
print(x, type(x))

# values()
y = d.values()
print(y,type(y))

# items()
z = d.items()
print(z,type(z))

# loop - for
# keys
for x in d:
    print(x)
for x in d.keys():
    print(x)
# values
for x in d:
    print(d[x])
for x in d.values():
    print(x)
# items
for x,y in d.items():
    print(x,y)

# changing value in dict
print(d)
# MIT --> AC
d["major"] = "AC"
print(d)
# update()
# 36 --> 26
d.update({"age":26})
print(d)

# add item to dict
d["university"] = "RUTS"
print(d)
d.update({"faculty":"MT"})
print(d)

# remove item in dict
# pop()
d.pop("university")
print(d)
#popitem()
d.popitem()
print(d)
# del keyword
if "majors" in d:
    del d["majors"]
else:
    print("No majors key in d.")
print(d)

# clear()
d.clear()
print(d)

# copy dictionary
x ={1:100, 2:200, 3:[3,30,300]}
print(x)

y = x
print(y)

x[1] = 1000
print(x)
print(y)

# copy()
y = x.copy()
print(y)
x[1] = 10
print(x)
print(y)

print(x)



