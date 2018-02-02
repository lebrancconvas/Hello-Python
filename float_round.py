# Change float number to round number
x = float(input("Input your float number : "))
index_after = str(x).find(".")
str_deci = (str(x))[index_after+1]
int_deci = int(str_deci)
first_index = (str(x))[:str(x).find(".")]
if(int_deci < 5):
  print(int(first_index))
else:
  print(int(first_index) + 1)