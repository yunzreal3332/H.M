#write program to rread values from user and print word "big"if value>10
value = int(input("Enter a value: "))
if value > 10:
    print("big")

#write program to rread values from user and print word "big"if value>10
#  and "small"  if value<=10
value = int(input("Enter a value: "))
if value > 10:
    print("big")
elif value <= 10:
    print("small")
#Write program to read the name from a user and print "you are exist"
#  if the name is exist in a list of names
#  otherwise will print "you are not exist.
names_list = ["Alice", "Bob", "Charlie", "David"]   
name = input("Enter your name: ")
if name in names_list:
    print("you are exist")
else:
    print("you are not exist")

#write program that doing summation of list of numbers
numbers = [5, 10, 15, 20, 25]
total_sum = 0
for num in numbers:
    total_sum += num
print("The summation of the list of numbers is:", total_sum)

