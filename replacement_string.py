def replaced_string():
    find_mark = line.find(marker)
    before_line_mark = line[:find_mark]
    before_replaced = before_line_mark + replacement
    after_line_mark_with_marker = line[find_mark:]
    after_line_mark = after_line_mark_with_marker[len(marker):]
    replaced = before_replaced + after_line_mark
    print("")
    print("OUTPUT SHOW!!!")
    print(">> ",replaced)

def game_replaced():
    print("WARNNING!! your word should be the word that occur in your line sentence.")
    line = input("Input your line sentence : ")
    marker = input("Input your word : ")
    replacement = input("Input your replacement word : ")
    replaced_string()

game_replaced()

"""
Result:

WARNNING!! your word should be the word that occur in your line sentence.
Input your line sentence :  Speaking Gently
Input your word :  Gently
Input your replacement word :  Rudely

OUTPUT SHOW!!!
>>  Speaking Rudely

"""
