#Write program to read a value between 0 and100 from user and
# print "Excellent"
# if the value is between or equal to [100,90],
# print "very Good"
# if the value is between or equal to [89,80], if the value is between or equal to [79,70]
# print "Good"
# if the value is between or equal to [69,60]
# print "Medium"
# print "Pass"
# if the value is between or equal to [59,50]
# print "Fail"
# if the value is leas than 50:
value = int(input("Enter a value between 0 and 100: "))
if 90 <= value <= 100:
    print("Excellent")
elif 80 <= value <= 89:
    print("Very Good")
elif 70 <= value <= 79:
    print("Good")
elif 60 <= value <= 69:
    print("Medium")
elif 50 <= value <= 59:
    print("Pass")
elif value < 50:
    print("Fail")