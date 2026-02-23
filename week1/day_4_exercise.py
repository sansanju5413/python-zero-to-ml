'''
1️⃣ Print Numbers 1 to 10
'''
for i in range(1,11):
    print(i)

'''
2️⃣ Print Even Numbers from 1 to 20

(Hint: use % 2 == 0)
'''
for i in range(1,21):
    if i%2==0:
        print(i)

'''3️⃣ Print Multiplication Table of 5'''
for i in range(5,9,5):
    for j in range(1,11):
        print(f"{i}x{j}={i*j}")
    print()

# 4️⃣ Sum of Numbers from 1 to 10
n=0
for i in range(1,11):
    n+=i
print("sum is: ", n)

#5️⃣ Find Largest Number in List (Without using max())
nums = [12, 45, 23, 89, 34]
largest=nums[0]
for num in nums:
    if num>largest:
        largest=num
print("largest value is: ", largest)

#3️⃣ Print all odd numbers from 1 to 50
for i in range(1,50,2):
    print(i)


#4️⃣ Print squares of numbers from 1 to 10
for i in range(1,11):
    print(f"square of {i} is {i*i}")

#5️⃣ Print multiplication table of any number (user input)
num=int(input("enter the number: "))
for n in range(1,11):
    print(f"{num}x{n}={num*n}")

''' 
6️⃣ Sum of numbers from 1 to n

(User enters n)
'''
n=int(input("enter the nth number: "))
total=0
for i in range(1,n):
    total+=i
print(f"total sum of {n-1}: {total}")

'''7️⃣ Factorial of a number

Example:
5! = 5 × 4 × 3 × 2 × 1
'''
n=int(input("enter the value for the factorial: "))
factorial=1
for i in range(1,n+1):
    factorial=factorial*i
print("factorial is: ", factorial)

#8️⃣ Count how many numbers between 1 and 100 are divisible by 3
for i in range(1,101):
    if i%3==0:
        print(i)

# 9️⃣ Reverse counting from 10 to 1
for i in range(10,0,-1):
    print(i)

'''
🔟 Count digits in a number

Example:
Input: 12345
Output: 5

(Hint: convert to string OR use while later)'''

n=input("enter a number: ")
count=0
for digit in n:
    count+=1
print(count)

# 1️⃣1️⃣ Find largest number in list (without max())
lis=[2,4,6,7,3,1,12]
large=0
for n in lis:
    if n>large:
        large=n
print(large)

#1️⃣2️⃣ Find second largest number in list
lis=[2,4,6,7,3,1,12]
large=0
seclarge=0
for n in lis:
    if n>large:
        large=n
print("largest number in the list is: ",large)
for i in lis:
    if i<n and i>seclarge:
        seclarge=i
print("second largest number in list is: ", seclarge)

'''
1️⃣3️⃣ Count vowels in a word

Input: "Sanju"
Output: 2
'''
word=input("enter your name: ")
vowel=["a", "e", "i" , "o" , "u"]
count=0
for letter in word.lower():
    if letter in vowel:
        count+=1
print("no.of vowels: ",count)

# 1️⃣4️⃣ Reverse a string using loop
st=input("enter the string: ")
reverse_text=" "
for i in st:
    reverse_text=i+reverse_text
print(reverse_text)


'''1️⃣6️⃣ Print this pattern:
*
**
***
****
*****
'''
for i in range(1,6):
    print("*"*i)

'''
1️⃣7️⃣ Print this pattern:
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