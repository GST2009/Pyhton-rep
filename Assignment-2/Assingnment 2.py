#TASK 1
A=int(input("Enter the number= "))
if(A%2==0):
    print(A,"is an even number")
else:
    print(A,"is odd number")

#TASK 2
A=0
for i in range(1,51):
    A+=i
print("the sum of numbers from 1 to 50 is: ",A)