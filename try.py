n = int(input("Enter a Number to create a pattern in python:"))
for i in range(0, n):
    for j in range(0, i+1):
        print("*", end=" ")
    print()