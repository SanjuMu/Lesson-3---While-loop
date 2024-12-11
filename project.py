n = m = int(input("Enter a number to findout number of digits in it: "))
x = 0

while n > 0:
    n = n // 10
    x = x+1
print("The total number of digits in ", m,"is", x)


