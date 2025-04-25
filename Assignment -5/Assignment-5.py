#Task1
Studentdata={"Alice":85,"James":40,"Bose":100}
Studentname=input("Enter the student name: ")
if Studentname in Studentdata:
    print(f"{Studentname}'s mark: {Studentdata[Studentname]}")
else:
    print("Student name not found")

#TASK 2
numbers = list(range(1, 11))
first_five = numbers[:5]
reversed_five = first_five[::-1]
print("First five elements:", first_five)
print("Reversed list:", reversed_five)
