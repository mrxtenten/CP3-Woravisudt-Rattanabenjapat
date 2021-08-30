usernameInput=input("Username : ")
passwordInput=input("Password : ")
if usernameInput=="born2admin" and passwordInput=="1todev":
    print("Done!")
    print("---Welcome to iEat shop---")
    print("1. water 10THB")
    print("2. sandwich 20THB")
    print("3. juice 15THB")
    print("4. Burger 40THB")
    userPick = int(input(">>"))
    if userPick==1:
        quantity1=int(input("How many : "))
        result1=quantity1*10
        print("water :",result1,"THB")
    elif userPick==2:
        quantity2=int(input("How many : "))
        result2=quantity2*20
        print("sandwich :",result2,"THB")
    elif userPick==3:
        quantity3=int(input("How many : "))
        result3=quantity3*15
        print("juice :",result3,"THB")
    elif userPick==4:
        quantity4=int(input("How many : "))
        result4=quantity4*40
        print("Burger :",result4,"THB")
    else:
        print("Error")
