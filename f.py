# loop
d=1
while c<3:
    c=c+1
print("loop ke ander")
print("loop ke bahar")



num=int(input("enter the number: "))
i=1
sum=0
while i<=10:
    num1=int(input("enter the number: "))
    sum=sum+num1
    i=i+1
print(sum)
    
       
num=int(input("enter the number: "))
i=1
product=0
while i<=num:
    num1=int(input("enter the number: "))
    product=product*num1
    i=i+1
print(product)n = int(input("Enter the value of 'n': "))


n=int(input("enter the number: "))
a = 0
b = 1
sum = 0
count = 1
print("Fibonacci Series: ", end = " ")
while(count <= n):
  print(sum, end = " ")
  count += 1
  a = b
  b = sum
  sum = a + b


n=int(input("enter the number: "))
fac=1
i=1
while i<=n:
    fac=fac*i
    i=i+1
print(fac)




n = int(input("Enter Number to calculate sum and average"))
totalNo = n
sum=0
while (n >= 0):
    sum += n
    n-=1
average  = sum / totalNo
print (sum)
print ( average)




num=int(input("enter the number: "))
temp=num
rev=0
while num>0:
    dig=num%10
    rev=rev*10+dig
    num=num//10
    if temp==rev:
        print("the number is palindrome!")
    else:
        print("not a palindrome!")


num=int(input("enter the number: "))
i=num
sum=0
while num>=0:
    sum=sum+num
    num=num-1
    average=sum/i
print(sum)
print(average)
    
timeings=(input("enter the time:-")
if timeings>="7:30":
    if timeings<="7:59" :
        print("breakfast")
    else:
        print("no breakfast")
elif timeings>="8:00":
    if timeings<="12:29":
        print("1st coding")
    else:
        print("empty")
elif timeings>="12:30":
    if timeings<="1:59":
        print("lunch")
    else:
        print("free time")
else:
    print("nothing")
    





