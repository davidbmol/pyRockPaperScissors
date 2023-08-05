import re

strInp = input("feladat? ")

#numRegex = re.compile(r'(\d+)(\+)?(\-)?(\/)?(\*)?(\d+)')
numRegex = re.compile(r'(\d+)(\+|\-|\/|\*?)(\d+)')
mo = numRegex.search(strInp)
#print(mo.group(1))

#num1, op_plus, op_sub, op_div, op_mult, num2 = mo.groups()
num1, op, num2 = mo.groups()
#ops = op_plus, op_sub, op_div, op_mult

print(op)

#number inputs switch to integer
int1 = int(num1)
int2 = int(num2)

#final result
if op == "+":
  number_sum=num_res = int1 + int2
elif op == "-":
  number_sub=num_res = int1 - int2
elif op == "/":
  number_div=num_res = int1 / int2
elif op == "*":
  number_mult=num_res = int1 * int2

result = round(num_res, 3)

#final prints (first number, operation, second number, solution)
print("first number:", num1)
print("operation: ", op)
print("second number:", num2)
print("result:", result)