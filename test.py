jparty = []
while True:
    insj = input("Insert your party : ")
    jparty.append(insj)
    for i in range(len(jparty)):
        print(i+1,jparty[i])
        if (len(jparty) >= 10):
            break
        else:
            continue