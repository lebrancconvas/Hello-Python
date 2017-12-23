try :
    print("Insert month number")
    print("January input '1'")
    print("Febuary input '2'")
    print("March input '3'")
    print("April input '4'")
    print("May input '5'")
    print("June input '6'")
    print("July input '7'")
    print("August input '8'")
    print("September input '9'")
    print("October input '10'")
    print("November input '11'")
    print("December input '12'")
    m = int(input(": "))
    if (m > 0 and m <= 12):
        if (m == 2):
            y = int(input("insert year : "))
            if (y % 4 == 0):
                print(29)
            else:
                print(28)
        elif(m == 4):
            print(30)
        elif(m == 6):
            print(30)
        elif(m == 9):
            print(30)
        elif(m == 11):
            print(30)
        else:
            print(31)
    else:
        print("--ERROR 404--")
except : 
    print("--ERROR 404--")
       
