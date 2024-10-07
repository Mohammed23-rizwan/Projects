# # # # Exercise 4: Remove first n characters from a string
# # # # Write a Python code to remove characters from a string from 0 to n and return a new string.

# # # # For Example:

# # # # remove_chars("PYnative", 4) so output must be tive. Here, you need to remove the first four characters from a string.
# # # # remove_chars("PYnative", 2) so output must be native. Here, you need to remove the first two characters from a string.
# # # # Note: n must be less than the length of the string.

# def nnumber(a,b):
#      c = a[b:]
#      return c
    
    
# a = input('enter A word to cut :')
# b = int(input('enter A word to cut :') )    
# d= nnumber(a,b)
# print(d)

# # Exercise 5: Check if the first and last numbers of a list are the same

# # Write a code to return True if the list’s first and last numbers are the same. If the numbers are different, return False.


# def fristchecking(number):
#     x = number[0]
#     y = number[-1]
#     if(x==y):
#         return True
#     else:
#         return False
    
# ans = [10,20,30,40,50,20]    
# d = fristchecking(ans)    
# print(d)

# Exercise 6: Display numbers divisible by 5
# Write a Python code to display numbers from a list divisible by 5

a = [10,20,54,56,25,22,15]

for nnum in a:
    if(nnum%5==0):
        print(nnum)