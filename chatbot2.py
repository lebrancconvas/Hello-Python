rom algorithm import Algorithm

def a1():
return {'a1': 42}
def a560():
return {'a560': 42}
def n():
return {'n': 560}
def sum_all(a1,a560,n):
s560 = n/2 # ตัวแปร s560 นำ n/2 คือ 560/2
a = a1+a560 # ตัวแปร a นำ a1+a560 คือ 42 + 42
return {'sum': s560*a} # คืนค่าผลลัพธ์ sum โดยนำ s560 มาคูณกับ a

blah = Algorithm(a1, a560, n, sum_all)
#print(blah.functions) ถ้าต้องการแสดงฟังก์ชันทั้งหมดที่มี
getsum = blah.run()
print(getsum['sum'])
[/python]