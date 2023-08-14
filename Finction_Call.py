# Taking input from the user
Num1 = int(input("Enter the first number: "))
Num2 = int(input("Enter the second number: "))

def multiply(num1, num2):
    result = Num1 * Num2
    return result
def add(num1, num2):
    result = num1+num2
    return result
def subtract(num1, num2):
    result = num1-num2
    return result
def devide(num1, num2):
    result = num1/num2
    return result

answer = multiply(Num1, Num2)
answer1 = add(Num1, Num2)
answer2 = subtract(Num1, Num2)
answer3 = devide(Num1, Num2)

print("The multiplication result is:", answer)
print("The multiplication result is:", answer1)
print("The multiplication result is:", answer2)
print("The multiplication result is:", answer3)
