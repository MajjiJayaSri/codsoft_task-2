num1 = int(input("Enter your first number : "))
num2 = int(input("Enter your second number : "))
op = input("Enter your operator (+,-,*,/,%,//,**): ")
if( op == '+'):
    print("The result after performing addition of",num1,"and",num2," is :",num1+num2)
elif op == '-':
    print("The result after performing subtraction of",num1,"and",num2,"is :",num1-num2)
elif op == '*':
    print("The result after performing multiplication of",num1,"and",num2,"is :",num1*num2)
elif op == '/':
    print("The result after performing division of",num1,"and",num2," is :",num1*num2)
elif op == '%':
    print("The result after performing modulus of",num1,"and",num2,"is :",num1%num2)
elif op == '//':
    print("The result after performing floor division of",num1,"and",num2,"is :",num1//num2)
elif op == "**":
    print("The result after performing exponentiation of",num1,"and",num2,"is :",num1**num2)
else:
    print("Invalid operator")