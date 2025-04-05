#TASK 1
A=int(input("Enter a number:"))
def factorial(A):
    if A<2:
        return 1
    else :
        return A*(factorial(A-1))

answer=factorial(A)
print("Factorial of",A,"is:",answer)

#TASK 2
import math
B=int(input("Enter a number:"))
Squareroot=math.sqrt(B)
print("Square root:",Squareroot)
Logarithm=math.log(B)
print("Logarithm:",Logarithm)
Sine=math.sin(B)
print("Sine:",Sine)