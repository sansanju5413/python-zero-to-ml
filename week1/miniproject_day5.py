'''
🎯 Mini Project: Number Analyzer (Single Run Version)
📌 Problem Statement

Build a program that:

Takes a number from user.

Prints:

Even or Odd

Prime or Not Prime

Palindrome or Not

Sum of digits

Factorial (if number ≤ 10, otherwise print "Too large")
'''

num=int(input("Enter number: "))
if num%2==0:
    print(f"{num} is even")
else:
    print(f"{num} is odd")

# Prime or Not Prime
if num<=1:
    print(f"{num} is not prime")
else:
    for i in range(2, num):
        if num%i==0:
            print(f"{num} is not a prime number")
            break
    else:
        print(f"{num} is a prime number")

# Palindrome or Not
num=str(num)
original=num
reverse=""
for i in str(num):
    reverse=i+reverse
if num==reverse:
    print(f"{num} is a palindrome")
else:
    print(f"{num} is not a palindrome")

#Sum of digits

n=str(num)  #needs to convert from int to string 
add=0
for i in n:
    add+=int(i)
print(add)

#another type
a=str(num)  #convert int to str
summ=0
for i in range(len(str(a))): 
    summ+=int(a[i])
print(summ)

#Factorial (if number ≤ 10, otherwise print "Too large")
num=int(num)
factorial=1
if num<0:
    print("factorial not defined")
elif num<=10:
    for i in range(1,num+1):
        factorial=factorial*i
    print(factorial)
else:
    print("Too large")


    


    
    


