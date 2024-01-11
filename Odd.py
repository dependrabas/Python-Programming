def oddNumber():
    n=1
    while True:
        yield n
        n += 2
odds = oddNumber()
for i in range(100):
 print(i)
