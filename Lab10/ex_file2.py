"""
Name: Puriwat Lertkrai
ID: 1111111111111
Group: MIT421
"""

# create file
import os
# create empty file
try:
    f = open("test2.txt","x")
    f.close()
except:
    print("File already exits.")

# create test3.txt on desktop of your computer
#C:\Users\Puriw\OneDrive\Desktop
try:
    f = open("C:\\Users\Puriw\OneDrive\Desktop\\test3.txt","x")
    f.close()
except Exception as e:
    print(e)


# write file
# mode "a" , "w"
try:
    f = open("test2.txt","w")
    f.write("Puriwat Lertkrai\n")
except:
    print("Cloud not found a fine name 'test2.txt")
finally:
    f.close()

# delete file

if os.path.exists("test3.txt"):
    os.remove("test3.txt")
else:
    print("File not found.")

