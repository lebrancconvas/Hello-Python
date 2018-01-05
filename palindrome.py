def palindrome():
    s = input("Insert your string :: ")
    if (s == s[::-1]):
        print(s , " is palindrome")
    else:
        print(s , " is not palindrome")
palindrome()

