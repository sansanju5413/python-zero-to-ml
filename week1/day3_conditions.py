#🚀 DAY 3 – Decision Making (If–Else Mastery)
#if Statement-->
'''if statement is used to test the condition , if the condition is True , the block of code under the if statement is executed

if condition:
    #code block to execute if the condition is true'''

#ex--->
time=9
if time==9:
    print("college timings")

#else Statement--->
'''else statement is provides an alternative block of code to execute when the if condition is False
if condition:
    block of code executes if the condition is True
else:
    block of code is executes, when the if condition is False
'''
time=10
if time==9:
    print("college time")
else:
    print("not a college college time")

# elif Statement-->
''' it is a short of "else if " statement to check the another condtion is if the previous if or elif condition is False, we can use multiple elif statement for the condition in the code
if condition1:
    # Code block if condition1 is True
elif condition2:
    # Code block if condition2 is True
else:
    # Code block if none of the above conditions are True'''

#ex-->
time=1
if time==9:
    print("college timings")
elif time==12:
    print("break time")
elif time==1:
    print("lunch time")
else:
    print("timings is not fixed ")

#comparision operators in the if statement
#used to compare the values in the if statement
'''
==: Equal to
!=: Not equal to
<: Less than
>: Greater than
>=: Greater than or equal to
<=: Less than or equal to
'''

#vote eligibility
age=float(input("enter your age: "))
if age>=18:
    print("you are eligible for vote")
else:
    print("you are not eligible for vote")


#Logical Operators in if Statements
'''You can also use logical operators to combine multiple conditions in if statements:

and: Returns True if both conditions are True
or: Returns True if at least one condition is True
not: Reverses the result of a condition
'''

#ex--->
age=float(input("enter your age: "))
is_indian_citizen=True

if age>=18 and is_indian_citizen:
    print("eligible for vote")
else:
    print("you are not eligible for vote")

#ksrts
age=int(input("enter your age: "))
gender="female"
if gender=="female":
    print("bus ticket is free")
elif age<=12:
    print("half ticket")
elif age>=60:
    print("senior citizen")
else:
    print("full ticket")

# Nested if Statements
'''use the if statement iside the if statement in the codition'''


day=input("enter the day")
raining=False
if day=="sunday":
    if raining:
        print("not go")
    print("you can go")
else:
    print("not go today")


#even or odd
num=int(input("enter number: "))
if num%2==0:
    print("number is even")
else:
    print("number is odd")

'''2️⃣ Biggest of Two Numbers

Take two numbers → print which is bigger.'''
a=int(input("enter value of a: "))
b=int(input("enter value of b: "))

if a>b:
    print("a is bigger than b")
elif a==b:
    print(" a and b are equal")
else:
    print("b is greater than a")

'''
3️⃣ Grade Calculator

Take marks → print:

Marks	Grade
>= 90	A
>= 75	B
>= 50	C
< 50	Fail
'''
marks=int(input("enter your marks: "))
if marks>=90:
    print("A grade")
elif marks>=75:
    print("B grade")
elif marks>=50:
    print("C grade")
else:
    print("Fail")

'''
4️⃣ Positive / Negative / Zero

Take number → identify type.
'''
n=float(input("enter number: "))
if n>0:
    print("number is positive")
elif n==0:
    print("number is zero")
else:
    print("negative")