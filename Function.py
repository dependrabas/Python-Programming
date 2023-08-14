# Taking input from the user
Num1 = int(input("Enter the first number: "))
Num2 = int(input("Enter the second number: "))

def multiply(num1, num2):
    result = num1 * num2
    return result

answer = multiply(Num1, Num2)

print("The multiplication result is:", answer)
