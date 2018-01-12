import random
while True:
    text = input("> ")
    a = ['HI','Hello','Hi','hI','hi','HELLO','hello','สวัสดีครับ']
    b = ['Hello :D','Hi',':D']
    c = ['What is your name?']
    d = ['Cherry','Charm','Pytho']
    if text in a:
        print(random.choice(b))
        continue
    else:
        print("?")

    if text in c:
        print(random.choice(d))
    else:
        print("?")