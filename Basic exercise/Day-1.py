# Exercise 1: Calculate the multiplication and sum of two numbers
# Given two integer numbers, write a Python code to return their product only if the product is equal to or lower than 1000. Otherwise, return their sum.

A = int(input("Enter a value of A :"))
B = int(input("Enter a value of B :"))

def multiply(a,b):
    c= a*b
    if(c<=1000):
        return c
    else:
        return a+b

C = multiply(A,B)

print(C)

# Exercise 2: Print the Sum of a Current Number and a Previous number
# Write a Python code to iterate the first 10 numbers, and in each iteration, print the sum of the current and previous number.

first_num = 0 

for i in range(10):
    a= first_num +i
    print(a)
    first_num = i
