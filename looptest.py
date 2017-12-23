def for_loop():
    month = "January" , "February" , "March" , "April" , "May" , "June" , "July" , "August" , "September" , "October" , "November" , "December"
    for m in range(len(month)):
        print(m + 1,"->",month[m])
        
def nested_loop():
    for a in range(1,13,1):
        print("------------")
        for b in range(1,13,1):
            print(a,"x",b,"=",a*b)
for_loop()
nested_loop()