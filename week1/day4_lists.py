#lists-->
'''
list is a collection of items that are ordered , mutable and allow duplicate elements.
list can hold items of different data types like integer , string, or even other lists. '''

# my_list=[element1, element2, element 3,...]
#eg-->
fruits=["apple", "banana", "cherry", "kiwi"]
number=[1,2,3,4,5]
mix=["apple", 2, True]


## Basic List Operations--->
#1. create a list-->
fruits=["apple", "banana", "cherry", "kiwi"]
number=[1,2,3,4,5]

#2.  Access Elements (Indexing)-->
print(fruits[0])
print(fruits[-1])

#3. Modifying Lists 
# i) Change specific value
fruits[2]="orange"
print(fruits)

number[-1]="text"
print(number)

#ii)  Adding elements:--->
#append(): Adds an element to the end of the list.
fruits.append("grapes")
print(fruits)

#insert(): Inserts an element at a specific index.
fruits.insert(1,"mango")
print(fruits)

fruits.insert(-1,"guva")
print(fruits)

#iii) Removing elements:--->
# remove(): Removes the first occurrence of an element.
fruits.remove("kiwi")
print(fruits)

# pop(): Removes the element at a specific index (or the last item if no index is provided).
fruits.pop()
print(fruits)

fruits.pop(2)
print(fruits)

# clear(): Removes all elements from the list.
fruits.clear()
print(fruits)  #clear or remove whole list 


# Slicing Lists--->
#You can extract a portion of a list using slicing.
'''
start: The index to start the slice (inclusive).
stop: The index to stop the slice (exclusive).
step: The number of steps to skip elements (default is 1).
'''

numbers=[1,2,3,4,5,6,7,8]
print(numbers[0:5:2]) #start:stop:step

fruits=['apple', 'mango', 'banana', 'orange', 'kiwi', 'guva', 'grapes']
print(fruits[0:5:2])  #include 0 to 5(excludes 5) and jump 2 output:['apple', 'banana', 'kiwi']
print(fruits[:5:2])  #it takes 0 auto if we not define , output:['apple', 'banana', 'kiwi']
print(fruits[::2])  #  output:['apple', 'banana', 'kiwi', 'grapes']

# Lists Functions:-->
# Length of List-->len(list)-->returns number of elements in the list
fruits=['apple', 'mango', 'banana', 'orange', 'kiwi', 'guva', 'grapes']
print(len(fruits))  # output: 7

#sorted(list):--->
#  Returns a new sorted list without changing the original list.
n=[5,6,7,8,9,1,2,3,4]
print(sorted(n))
print(n)

#sum(list)-->
#  Returns the sum of elements in a list (for numerical lists).
print(sum(n))  #output: 45

# lists Methods-->
#1. index(element)--> Returns the index of the first occurrence of the specified element.
fruits=['apple', 'mango', 'banana', 'orange', 'kiwi', 'guva', 'grapes']
print(fruits.index("apple"))  #output: apple

#count(element)-->
# returns the number of occurence of the element in the list.
num=[1,2,3,4,56,1,4,1,1,3]
print(num.count(1))

#reverse(): Reverses the elements of the list in place.
n=[3,4,56,4]
n.reverse()
print(n)  #output: [4, 56, 4, 3]

#sort()-->
#sort the list in place(ascending order by default)
n=[4,5,8,1,9,3]
n.sort()  #ascending order
print(n)  #output:[1, 3, 4, 5, 8, 9]
n.reverse()  #descendind order
print(n) #output:[9, 8, 5, 4, 3, 1]


# Nested lists-->
#Lists can contain other lists, allowing you to create nested lists. This can be useful for storing matrix-like data structures.
matrix=[
    [1,2,3],  #-->oth index
    [4,5,6], #-->1st index
    [7,8,9] #2nd index
]
print(matrix[0]) # output: [1, 2, 3]
print(matrix[1][1])  #output:5
print(matrix[1::]) #output:[[4, 5, 6], [7, 8, 9]]
