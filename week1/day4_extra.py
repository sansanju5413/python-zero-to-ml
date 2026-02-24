#1️⃣ Sum of even numbers from 1 to n
even=0
n=int(input("enter the n number: "))
for i in range(1,n+1):
    if i%2==0:
        even+=i
print(even)

#2️⃣ Product of numbers from 1 to n
n=int(input("enter n number: "))
product=1
for i in range(1,n+1):
    product*=i
print(product)

#3️⃣ Count how many numbers in a list are greater than 50
lis=[1,4,5,8,67,45,32,98,100,56,78,-67]
count=0
for i in lis:
    if i>50:
        count+=1
print(count)


# 4️⃣ Find smallest number in list (without min())
listss=[]
for i in range(0,5):
    nu=int(input("enter the number: "))
    listss.append(nu)
print(listss) #for my convinient
smallest=listss[0]
for number in listss:
    if number<smallest:
        smallest=number
print(smallest, "is the smallest number in the list")


'''
*
**
***
****
*****
'''
for i in range(1,6):
    print("*"*i)

'''
1
12
123
1234
12345
'''
for i in range(1,6):
    for j in range(1,i+1):
       print(j,end="")
    print()

# 5️⃣ Check if a number is palindrome
num=(input("enter the number: "))
reverse=""
for digit in num:
    reverse=digit+reverse

if num==reverse:
    print("it is a palindrome")
else:
    print("not a palindrome")


#👉 Write a program to check if a number is PRIME.
num = int(input("Enter number: "))
if num <= 1:
    print(f"{num} is not a prime")
else:
    for i in range(2,num):
        if num%i==0:
            print(f"{num} is not a prime number")
            break
    else:
        print(f"{num} is a prime number")
        