a=int(input("enter the number: "))
b=int(input("enter the number: "))
while a%b!=0:
    s=a%b
    a=b
    b=s
    print(b,"HCF")