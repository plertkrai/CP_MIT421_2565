"""
Student name: Puriwat Lertkrai
ID: 001
Group: MIT421
"""


# comment
# 1. one-line  --> #
# 2. multi-line  --> """...."""

# Variable
# integer คือ จำนวนเต็ม  -2 -1 0 1 2
x = 10
print(x)
print(type(x))
y = 20
print(x+y)  #30
print("x+y="+str(x+y))
print("x+y=",x+y)
# f string
print(f'x+y={x+y}')
z = x+y  # 30
print(z,type(z))

# assign multiple variable
a,b,c = 10,20,30
print(a)
print(b)
print(c)
print(a,b,c)
a = b = c = -10
print(a,b,c)

# float  คือ ข้อมูลประเภทจำนวนจริง เช่น -2.2 -1.1 0.0 1.1 2.2
x = 10.10
print(x,type(x))
x = int(x)   # convert type float to int
print(x,type(x))

# String(str) คือ ข้อมูลประเภทข้อความ  เช่น "MIT" 'RUTS'
msg = "Hello, I am Student at MT"
print(msg,type(msg))
# concatenation string (+)
msg2 = "I am studying in MIT major"
print(msg+msg2)
print(msg+" "+msg2)
print(msg,msg2)
# function built-in in class str
# len() นับจำนวนตัวอักษรของข้อความ หรือความยาวของสมาชิกในตัวแปร  -> int
print(len(msg))
print(len(msg2))
# split() ใช้สำหรับการตัดคำโดยสัญลักษณ์แล้วเอาข้อความมาเก็บไว้ใน list
myword = msg.split(" ")
print(myword,type(myword))
print(len(myword))

# boolean(bool) คือ ตัวแปรที่เก็บค่าความจริง --> True,False (1,0)
a = True
print(a,type(a))

x = 100
# หากนำตัวแปรที่มีค่าข้อมูลที่ไม่ใช่ None จะได้ค่า True เสมอ
y = bool(x)  # convert int to bool
print(y,type(y))

print(bool(0))  # False
print(bool(100)) # True
print(bool(-100)) # True

bool = 10
print(bool)
def = 10
print(def)
