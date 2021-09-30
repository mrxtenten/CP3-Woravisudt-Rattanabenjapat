menuList = []
def showBill():
    total = 0
    print("---My Food---")
    for number in range(len(menuList)):
        print(menuList[number])
        total += int(menuList[number][1])
    print("price : ",total)

while True:
    menuName = input("Please Enter Menu : ")
    if(menuName.lower() == "exit"):
        break
    else:
        menuPrice = input("Price : ")
        menuList.append([menuName,menuPrice])

showBill()