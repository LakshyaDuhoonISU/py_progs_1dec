#WAP to find largest among three numbers
a=float(input("Enter first number: "))
b=float(input("Enter second number: "))
c=float(input("Enter third number: "))
if a>b:
    if a>c:
        print(a,"is the largest among them.")
    else:
        print(c,"is the largest among them.")
else:
    if b>c:
        print(b,"is the largest among them.")
    else:
        print(c,"is the largest among them.")
