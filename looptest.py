def for_loop():
    month = "January" , "February" , "March" , "April" , "May" , "June" , "July" , "August" , "September" , "October" , "November" , "December"
    for m in range(len(month)):
        print(m + 1,"->",month[m])
        
def nested_loop():
    for a in range(1,13,1):
        print("------------")
        for b in range(1,13,1):
            print(a,"x",b,"=",a*b)
            
def while_loop():
    password = "lebconv"
    while True:
        p = input("Input your password : ")
        if (p != password):
            print("--WRONG, Please try again--")
        else:
            print("You pass!!, Welcome to my website.")
            break
            
def loop_test():
    while True:
        m = int(input("Insert your money : "))
        if (m < 500):
            while True:
                name = input("Input your name (Max 20 Char) : ")
                if (len(name) <= 20):
                    print("Ok , " , name , "I think you should try to spend less.")
                    break
                else:
                    print("--ERROR , Insert your name again--")
                    continue
            break
        else:
            print("Ok! Good job. Now you have ",m," Bath")
            break
                
    
    
for_loop()
nested_loop()
while_loop()
loop_test()