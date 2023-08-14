def is_palindrome(string):
   return string[::-1].casefold() == string.casefold()

word  = input("please enter a word to check:")
if is_palindrome(word):
    print(" '{}' is a palindrone ".format(word))
else:
    print(" '{}' is not a palindrone ".format(word))