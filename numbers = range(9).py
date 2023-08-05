import re
#str.isnumeric("+")

strInp = input("feladat?") 
#operations = {"+","-","/","*"}

phoneNumRegex = re.compile(r'(\d\d)(\+)?(\-)?(\/)?(\*)?(\d\d)')
mo = phoneNumRegex.search(strInp)
print(mo.group(1))

num1, op_plus, op_sub, op_div, op_mult, num2 = mo.groups()
ops = op_plus, op_sub, op_div, op_mult

print("first number:", num1)
#print("operation:", ops)
if op_plus:
  print("operation: +")
elif op_sub:
  print("operation: -")
elif op_div:
  print("operation: /")
elif op_mult:
  print("operation: *")
print("second number:", num2)