#WAP to perform arithmetic calculation. This program accepts two operands and an operator then displays the calculated result.
a=float(input("Enter first number: "))
b=float(input("Enter second number: "))
c=input("Select the operator: +,-,/,*,%,//,** ")
if c=="+":
    print("Sum:",a+b)
elif c=="-":
    print("Difference:",a-b)
elif c=="*":
    print("Multiplication:",a*b)
elif c=="/":
    print("Division:",a/b)
elif c=="%":
    print("Remainder:",a%b)
elif c=="//":
    print("Floor division:",a//b)
elif c=="**":
    print("Power:",a**b)
else:
    print("Invalid operator!")