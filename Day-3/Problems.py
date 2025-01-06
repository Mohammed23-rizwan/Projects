#leetcode problem 

#412. Fizz Buzz

n= int(input("enter a number : "))

same = []

for i in range(1,n+1):
    if(i%15 == 0):
        same.append('fizzBuzz')
    elif(i%5 == 0):
        same.append('buzz')
    elif(i%3==0):
        same.append ('fizz')
    else:
        same.append(str(i))        
        
print(same)        
        
        
n=[1,2,3,4,5,6,7,8,9]        

for i in n:
    print (n[i])