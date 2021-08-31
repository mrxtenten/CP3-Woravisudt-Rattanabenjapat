number=int(input())
text=""
for x in range(number):
    gap = " " * number
    number -= 1
    text=text+"*"
    print(gap,text)
    text=text+"*"