"""
Name: Puriwat Lertkrai
ID: 1111111111111
Group: MIT421
"""
print("Start")

def division(a,b):
        return a/b
        raise ZeroDivisionError("divide by zero")

try:
    rs = division(10,0)
    print("The result: ",rs)
except Exception as e:
    print("Error log: ",e.args)


print("End")