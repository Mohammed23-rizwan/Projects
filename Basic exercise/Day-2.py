# # # # # Exercise 4: Remove first n characters from a string
# # # # # Write a Python code to remove characters from a string from 0 to n and return a new string.

# # # # # For Example:

# # # # # remove_chars("PYnative", 4) so output must be tive. Here, you need to remove the first four characters from a string.
# # # # # remove_chars("PYnative", 2) so output must be native. Here, you need to remove the first two characters from a string.
# # # # # Note: n must be less than the length of the string.

# # def nnumber(a,b):
# #      c = a[b:]
# #      return c
    
    
# # a = input('enter A word to cut :')
# # b = int(input('enter A word to cut :') )    
# # d= nnumber(a,b)
# # print(d)

# # # Exercise 5: Check if the first and last numbers of a list are the same

# # # Write a code to return True if the list’s first and last numbers are the same. If the numbers are different, return False.


# # def fristchecking(number):
# #     x = number[0]
# #     y = number[-1]
# #     if(x==y):
# #         return True
# #     else:
# #         return False
    
# # ans = [10,20,30,40,50,20]    
# # d = fristchecking(ans)    
# # print(d)

# # Exercise 6: Display numbers divisible by 5
# # Write a Python code to display numbers from a list divisible by 5

# a = [10,20,54,56,25,22,15]

# for nnum in a:
#     if(nnum%5==0):
#         print(nnum)

# Exercise 7: Merge three lists using the following condition

def resolution(num1,num2,num3):
    list4=[]
    for b in num1:
        list4.append(b)
    for c in num2:
        list4.append(c)   
    for d in num3:
        list4.append(d)                
    print(list4)
num1 =[10,20,30,40,50]
num2 =[60,70,80,90,100]
num3 =[110,120,130,140,150]
d = resolution(num1,num2,num3)

