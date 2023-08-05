#Python Calculator
import re


#num1 = int(input("first number?"))
#num2 = int(input("second number?"))
#numbers = [num1, num2]
operation = input("operation?")=="+"
num_res=0
strInp = input("feladat?")

if operation == "+":
  number_sum=num_res = num1 + num2
  #print(number_sum)
elif operation == "-":
  number_sub=num_res = num1 - num2
  #print(number_sub)
elif operation == "/":
  number_div=num_res = num1 / num2
  #print(number_div)
elif operation ==  "*":
  number_mult=num_res = num1 * num2
  #print(number_mult)

print(num_res)  

print(strInp[1])

parseRegex = re.compile(r'(\d)+(\d)+')
print(re.search(strInp))
