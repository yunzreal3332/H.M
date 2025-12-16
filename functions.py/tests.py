#If you have list of values, write program to count the
#number that divisible by 3.
List=[12, 45, 23, 67, 78, 90, 11, 9, 3, 4, 5, 6]
count=0
for i in List:
    if i%3==0:
        count+=1
print("Number of elements divisible by 3:", count)
#If you have list of values, write program to select the
#minimum number and the maximum number.
List=[12, 45, 23, 67, 78, 90, 11, 9, 3, 4, 5, 6]
minimum=List[0]
maximum=List[0]
for i in List:
    if i<minimum:
        minimum=i
    if i>maximum:
        maximum=i
print("Minimum number:", minimum)
print("Maximum number:", maximum)
#If you have list of values, write program to sum all the
#elements in the list.
List=[12, 45, 23, 67, 78, 90, 11, 9, 3, 4, 5, 6]
sum=0
for i in List:
    sum+=i
print("Sum of elements:", sum)
#If you have list of values, write program to select the
#minimum number and the maximum number using while loop.
List=[12, 45, 23, 67, 78, 90, 11, 9, 3, 4, 5, 6]
minimum=List[0]
maximum=List[0]
i=0
while i<len(List):
    if List[i]<minimum:
        minimum=List[i]
    if List[i]>maximum:
        maximum=List[i]
    i+=1
print("Minimum number:", minimum)
print("Maximum number:", maximum)

