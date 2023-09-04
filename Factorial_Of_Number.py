#Program to find factorial of number
a=int(input("Enter a number"))
b=1
for i in range(a,1,-1):
      b=b*i


print("The factorial of", a, "is", b)
