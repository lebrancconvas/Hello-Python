def string(s):
    for i in range(len(s)):
        print("{:>7}".format(i),end="")
    print()
    for i in range(-len(s),0,1):
        print("{:>7}".format(i),end="")
    print()
    for i in s:
        print("{:>7}".format(i),end="")
    print()

string("Agoda")
print("-" * 65)
string("Macrosman")
print("-" * 65)
string("Geronemo")
