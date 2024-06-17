a=int(input("enter a number:"))
sum=0
while(a!=0):
    lastdigit=a%10
    sum=lastdigit+sum
    a=a//10
print(sum)


