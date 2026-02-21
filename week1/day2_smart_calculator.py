'''🧮 Smart Calculator
Problem:

Ask user:

First number

Second number

Print:

Addition

Subtraction

Multiplication

Division

Modulus

Power

Also print:

Is first number greater than second?

Are both numbers equal?

You must use:

Arithmetic operators

Comparison operators

Logical operators (small usage)'''

print("SMART CALCULATOR")
firstnum=float(input("enter first number: "))
secnum=float(input("enter second number: "))

print("addition is: ", firstnum+secnum)
print("subtraction is: ", firstnum-secnum)
print("multiplication is: ", firstnum*secnum)
print("division is: ", firstnum/secnum)
print("floor division is: ", firstnum//secnum)
print("modulus is: ", firstnum%secnum)
print("power is: ", firstnum**secnum)

print("Is first number greater than second?", firstnum > secnum)
print("Are both numbers equal?", firstnum == secnum)

print("is first number is greator and not equal to second?", firstnum>secnum and firstnum!=secnum)