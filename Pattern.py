Num = int(input("Enter a Number to print a pattern:"))
for i in range(1,Num+1):
    print(" " *(i-1),end="")
    print("*" * (2*(Num-i)+1))