print("*" *30)
print()
print("Welcome to online voting checking...")

Name = input("Please enter your Name:")
Age = int(input("Enter your Age:"))
if Age>18:
    print("{} you not Eligible  for Voting".format(Name))
else:
    print("{} your are Eligible for Voting".format(Name))