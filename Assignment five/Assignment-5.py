#Task1
Studentdata={"Alice":85,"James":40,"Bose":100}
Studentname=input("Enter the student name: ")
if Studentname in Studentdata:
    print(f"{Studentname}'s mark: {Studentdata[Studentname]}")
else:
    print("Student name not found")

#TASK 2
List=input("Original list: ")
firstfive=List[0:9]
print("Extracted first five elements: ",List[0:9])
print("Extracted last five elements:  ",firstfive[::-1])
