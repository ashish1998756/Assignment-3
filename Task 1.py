# Task 1: Calculate Factorial Using a Function


def factorial(x):
    if x<2:
        return 1
    else:
        return x*factorial(x-1)

val=int(input("Enter a number:"))
print("Factorial of", val , "is :", factorial(val) )


