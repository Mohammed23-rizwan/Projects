import math

a= float(input("enter a A value : "))
b= float(input("enter a B value : "))

result = pow(a,2)+pow(b,2)
result = math.sqrt(result)

print(f"The hypotenuse of right triangle is : {round(result,2)}")