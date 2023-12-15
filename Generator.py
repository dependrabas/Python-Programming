import sys

def my_range(n: int):
  print(("my_range starts")
  start = 0
  while start < n:
       print(("my_range returning {}".format(start))
    yield start
    start += 1
_= input ("Line 12")
big_range = my_range(5)
_= input("Line 15")
big_list = []
_= input("Line 22")


for val in big_range:
    _= input("Line 24 inside loop")

print("The big_range is {} bytes.".format(sys.getsizeof(big_range)))
print("Big_List is {} bytes".format(sys.getsizeof(big_list)))
print(big_range)
print(big_list)
