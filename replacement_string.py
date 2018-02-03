print("WARNNING!! marker should be the word that occur in line.")
marker = input("Input your word : ")
replacement = input("Input your replacement word : ")
line = input("Input your line sentence : ")


find_mark = line.find(marker)
before_line_mark = line[:find_mark]
before_replaced = before_line_mark + replacement
after_line_mark_with_marker = line[find_mark:]
after_line_mark = after_line_mark_with_marker[len(marker):]
replaced = before_replaced + after_line_mark


#print(before_line_mark)
#print(after_line_mark_with_marker)
#print(after_line_mark)
#print(before_replaced)
print(replaced)