"""

เขียนโปรแกรมเพื่อรับค่าอินพุตจากผู้ใช้เป็นเลขจำนวนเต็ม
จำนวน 2 ชุดข้อมูล โดยมีข้อมูลชุดละ 10 ตัว
จากนั้นให้แสดงข้อมูลที่ซ้ำกัน และไม่ซ้ำกันจากข้อมูล 2 ชุดนี้
ทางหน้าจอภาพ
"""


s1 = set()
for i in range(5): # 0-9
    x = int(input(f"(set 1) enter an integer {i+1}: "))
    s1.add(x)
print(s1)

s2 = set()
for i in range(5): # 0-9
    x = int(input(f"(set 2) enter an integer {i+1}: "))
    s2.add(x)
print(s2)

print("same integer between s1 and s2: ",s1.intersection(s2))
print("difference integer between s1 and s2: ",s1.symmetric_difference(s2))
