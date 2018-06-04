money = 10000000
while True:
    print("I'm Jisso The Money Machine , Can I help you?")
    print("Wanna Deposit insert 'd'")
    print("Wanna Whitdraw insert 'w'")
    print("Wanna Exit from my program insert '0'")
    ins = input("What do you want from me >>> ")
    if(ins == "d"):
        dm = int(input("How many do you wanna deposit >>> "))
        money = money + dm
        print(">>> Now you have ",money,"Baht <<<")
        print("--------------------")
    elif(ins == "w"):
        wm = int(input("How many do you wanna withdraw >>> "))
        if (wm <= money):
            money = money - wm
            print(">>> Now you have ",money,"Baht <<<")
            print("--------------------")
        else:
            print("Sorry you dont have enough money to withdraw")
            print(">>> Now you have ",money,"Baht <<<")
            print("--------------------")
    elif(ins == "0"):
        print("You sure to exit??")
        print("Sure insert 'y'")
        print("Not Sure insert 'n'")
        ext = input(">>> ")
        if (ext == "y"):
            print(">>> Summarize your money : ",money,"Baht <<<")
            print("Thank you, C U Again")
            break
        elif (ext == "n"):
            print("Ok, So I'ii return you to menu again")
            print("--------------------")
            continue
        else:
            print("I don't know what you want to do??")
            print("--------------------")
    else:
        print("ERROR404 -- I can't help you -- Please Try Again")