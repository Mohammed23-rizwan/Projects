#python operator

operator = input("Enter an operator (+ - * /) to perform : ")
a= float(input("enter the value of A is : "))
b= float(input("enter the value of B is : "))

if operator == '+':
    print(f'Your entered addition operator : {a+b}')
elif operator == '-':
    print(f'Your entered addition operator : {a-b}')
elif operator == '*':
    print(f'Your entered addition operator : {a*b}')
elif operator == '/':
    print(f'Your entered addition operator : {a/b}')           
else:
    print("Please enter a valued operator")     