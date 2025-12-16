#compute the root of a quadratic equation
import math
a = 1
b = -3
c = 2
discriminant = b**2 - 4*a*c 
root1 = (-b + math.sqrt(discriminant)) / (2*a)
root2 = (-b - math.sqrt(discriminant)) / (2*a)
print("The roots of the quadratic equation are:", root1, "and", root2)  

#if statment exercises
#Write an if statement that asks for the user's name via input() function. 
# If the name is "Bond" make it print "Welcome on board 007."
#  Otherwise make it print "Good morning NAME". 
# (Replace Name with user's name)
name = input("Please enter your name: ")
if name == "Bond":
    print("Welcome on board 007.")
else:
    print("Good morning", name)

#Write an if statement that asks for the user's name via input() function
# and print True if a number is even and otherwise print False
number = int(input("Please enter a number: "))
if number % 2 == 0:
    print("True")
else:
    print("False")

#Write a Python program to find those numbers which are divisible by 7
#  and multiple of 5, between 1500 and 2700 (both included).
for num in range(1500, 2701):
    if num % 7 == 0 and num % 5 == 0:
        print(num)
#Write a Python program to find those numbers which are divisible by 7 or multiple of 5,
# between 1500 and 2700 (both included)
for num in range(1500, 2701):
    if num % 7 == 0 or num % 5 == 0:
        print(num)
#Write a Python program that accepts a word from the user and reverse it
word = input("Please enter a word: ")
reversed_word = word[::-1]
print("The reversed word is:", reversed_word)
