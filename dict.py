try:
    num = input("input your number : ");
    if float(num)<0:
        raise ValueError("Negative!");
    else:
        print("Ok! The Number is " + num);
except:
    print("WTF! Why error ?");
finally:
    print("Thank you for your participate.");

