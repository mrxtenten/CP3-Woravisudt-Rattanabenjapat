number=int(input())
text=""
for x in range(number):
    gap = " " * number
    number -= 1
    text=text+"*"
    print(gap,text)
    text=text+"*"

# ตัวอย่างของคนอื่น (บอกแล้ววิธีเขียนโปรแกรมมีหลายแบบ)
""" 
number = int(input("กรอกตัวเลข : "))
print("จำนวน",number,"แถว")
for i in range(number):
    print(" "*(number-i),"*"*(((i+1)*2)-1))
"""

"""
n = int(input())
space = n-1
star = 1
for i in range(n):
    print(" "*space,end="")
    print("*"*star)
    star+=2
    space-=1
"""