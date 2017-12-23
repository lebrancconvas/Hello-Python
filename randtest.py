import random
inp = int(input("Insert your predict value: "))
if(inp >= 0 and inp < 100):
    for i in range(9):
        value = random.randint(1,100)
        if (value == inp):
            print(value,"-> That's a right number")
        elif(value > inp):
            print(value,"-> Too much!!")
        elif(value < inp):
            print(value,"-> Too less")
        else:
            print("--ERROR--")
else:
    print("--ERROR--")
            
   