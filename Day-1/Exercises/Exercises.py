#1. Formatted Twinkle Poem

#Write a Python program to print the following string in a specific format (see the output).
#Sample String : "Twinkle, twinkle, little star, How I wonder what you are! Up above the world so high, Like a diamond in the sky. Twinkle, twinkle, little star, How I wonder what you are"
#Output :

#Twinkle, twinkle, little star,
#	How I wonder what you are! 
#		Up above the world so high,   		
#		Like a diamond in the sky. 
#Twinkle, twinkle, little star, 
#	How I wonder what you are

#Following answer is

#\n is used to insert a new line in that specif space 
#\t is used to tab the current line

print("Twinkle, Twinkle, little star,\n\tHow i wonder What you are!\n\t\tUp above the world so high\n\t\tLike a diamond in the sky,\nTwinkle, Twinkle, little star,\n\thow i wonder what you are")


#2. Python Version Checker

#Write a Python program to find out what version of Python you are using.
# sys is predefined function is used to check the version of python

import sys

print('Python Version:')
print(sys.version)
print('Python Version Info')
print(sys.version_info)

#3. Current DateTime Display

#Write a Python program to display the current date and time.
#Sample Output :
#Current date and time :
#2014-07-05 14:34:14

import datetime

now = datetime.datetime.now()

#datetime is predefined function in python
#strftime is used to reassigned liked your format

print(now.strftime('%Y-%m-%d %H:%M:%S'))

#4. Circle Area Calculator

#Write a Python program that calculates the area of a circle based on the radius #entered by the user.
#Sample Output :
#r = 1.1
#Area = 3.8013271108436504

r= float(input('enter a radius of circle :'))

#3.14159 is pi value
#formula of radius of circle is pi*r^2

area =3.14159*r*r

print(f"area of circle is : {area}")

#5. Reverse Full Name

#Write a Python program that accepts the user's first and last name and prints them in reverse order with a space between them.

firstname = input('Enter your first name :')
lastname = input('Enter your last name :')

print(f"hello {lastname} {firstname}")