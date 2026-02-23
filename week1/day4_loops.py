'''
hat Is a Loop?

A loop means:

👉 Repeat something multiple times
👉 Automatically
👉 Without writing the same code again and again
'''

'''
🔁 Two Types of Loops in Python

1️⃣ for loop
2️⃣ while loop
'''

# Understanding for Loop Clearly-->
# for loop allows you to repeat a block of code a fixed number of times , or once for each element in a sequence
'''
for variable in sequence:
    # code block
    '''


marks=[10,2,3,4,5]
for mark in marks:
    print(mark)

cities=["hassan", "mysure", "konanur", "hubli"]
for city in cities:
    print(city)

#using range() with for loops
'''
The range() function generates a sequence of numbers, which you can use in a for loop when you want to repeat a block of code a specific number of times.
Syntax of range():
range(start, stop, step)
start: The starting value (inclusive).
stop: The ending value (exclusive).
step: The increment (optional, default is 1).
'''
for i in range(5):
    print(i)


for i in range(0,11,2):
    print(i)

name="karnataka"
for letter in name:
    print(letter)


# Nested for Loops--->
'''
You can also have nested for loops, which means a loop inside another loop. This is useful when working with multi-level data, like lists inside lists.
'''
for i in range(1,6):
    for j in range(1,6):
        print(f"{i}x{j}={i*j}")
    print()

# Using break in a for Loop-->
#break statement is used to exit a loop early when a certain condition is met
#ex-->stop the loop when you find a specific item
cities=["banglore", "mysure", "shivamogga", "gadag"]
for city in cities:
    if city=="mysure":
        print(f"city found {city}")
        break
    print(city)

# Using continue in a for Loop--->
cities=["banglore", "mysure", "shivamogga", "gadag"]
for city in cities:
    if city=="mysure":
        continue
    print(city)