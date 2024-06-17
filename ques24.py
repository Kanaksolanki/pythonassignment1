a=int(input("enter a number:"))
b=int(input("enter another number:"))
c=(input("choose operator:"))
if c=="+":
    print("addition=",a+b)
elif c=="-":
    print("subtraction",a-b)
elif c=="*":
    print("multiplication=",a*b)
elif c=="/":
    print("division=",a/b)
else:
    print("invalid input")


