def login():
    usernameInput = input("Username : ")
    passwordInput = input("Password : ")
    if usernameInput == "admin" and passwordInput == "1234":
        return showMenu()
    else:
        print("username false")
        return login()
def showMenu():
    print("----iShop----")
    print("1. Vat Calculator")
    print("2. Price Calculator")
    return showSelect()
def showSelect():
    userSelected = int(input(">>"))
    if userSelected == 1:
        price3 = int(input("Price : "))
        return vatCalculate(price3)
    elif userSelected == 2:
        return priceCalculate()
    else :
        return showSelect()
def vatCalculate(totalPrice):
    vat = 7
    result = totalPrice + (totalPrice * vat / 100)
    return result
def priceCalculate():
    price1 = int(input("First Product Price : "))
    price2 = int(input("Second Product Price : "))
    return vatCalculate(price1 + price2)
print(login())