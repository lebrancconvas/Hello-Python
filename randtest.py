import random 
value = random.randint(1,99)
while True:
    try:
        inp = int(input("Insert your predict value(Only 0-99): "))
        if(inp >= 0 and inp < 100):
            for i in range(1):
                if (value == inp):
                    print("-> That's a right number")
                    print("Good Job , Thank you for participation.")
                elif(value < inp):
                    print("-> Too much!!")
                elif(value > inp):
                    print("-> Too less")
                else:
                    print("--ERROR--")
        else:
            print("--ERROR--")
    except:
        print("--End The Program--")
        break
        
        
            
   