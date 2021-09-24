def vatCalculate(totelPrice):
    result = totelPrice+(totelPrice*7/100)
    return result

price = int(input("ราคา: "))
print(vatCalculate(price))