#1) operators
#--->
'''Arithmatic operators
    addition-->+
    subtraction-->-
    multiplication-->*
    division-->/
    floor division-->//
    modulus-->%
    exponential-->**'''


#simple example-->
#assigning a value to the variable
a=100
b=10

print(a+b)  # Output:110
print(a-b) # Output:90
print(a*b) # Output:1000
print(a/b) # Output:10.0
print(a//b) # Output:10
print(a%b) # Output:0
print(a%b) # Output:0
print(a**b) # Output:100000000000000000000

#2. Assignment Operators-->
#used to assigning a value to the variable
'''
=: Assigns value on the right to the variable on the left.
+=: Adds right operand to the left operand and assigns the result to the left operand.
-=: Subtracts the right operand from the left operand and assigns the result to the left operand.
*=: Multiplies the left operand by the right operand and assigns the result to the left operand.
/=: Divides the left operand by the right operand and assigns the result to the left operand.
%=: Takes modulus of left operand by right operand and assigns the result to the left operand.

                                                                                        '''

#a-b-->a & b are the operands and '-'is the operator


#example-->
age=21 # the value 21 is assigned to the variable age
age+=4  # += means adding the vale to the varible like this age=age+4--->21+4=25
print(age)

# other operators also like this
age-=2
print(age)  #output-->25-2=23

age*=2
print(age)  #output--->23*2=46

age/=3
print(age)  #output-->46/3=15.333333333333334


# 3) Comparison Operators
    # comparision operators used to compare the two values, and they return True or False
'''
     == -->Checks if two values are equal.
    !=  -->Checks if two values are not equal.
    >   -->Checks if the left operand is greater than the right operand.
    <   -->Checks if the left operand is less than the right operand.
    >=  -->Checks if the left operand is greater than or equal to the right operand.
    <=  -->Checks if the left operand is less than or equal to the right operand.'''

a=15
b=23
print(a==b) #returns False
print(a!=b) #True
print(a>b) #False
print(a<b) #True
print(a>=b) #False
print(a<=b) #True


# 4) Logical Operators
    #logical statement are used to combine the conditions

'''
and-->returns True if the both conditions true
or-->returns True if the atleast one condition is true
not-->returns the reverse based on the condition like(if condition is true then returns False)
'''

a=12
b=3
c=4
print(a>b and c>b)  #returns true -->both conditions are true
print(a>b and b>c) #returns False -->a>b but b is not greater than c -->gives False

print(a>b or b>c) #returns True -->atleast one condtion is true
print(a>b or c>b) #both conditions are true gives-->True becouse atleast 1 condition needs to true if both conditions true than it will give true
print(b>a or c>a) #returns False -->both condtions are false

print(not(b>a)) # b is not greater than a but gives True becouse--> not(b>a)
print(not(a>b))  # here a > b but gives false -->becouse of not(a>b)

# 5) Miscelleneous operators-->
    #Membership operator-->
        #used to test within the sequence like within list , tuple,string. returns the True or False
    

    # in--> if the specified value is there in the sequence returns true
num=[1,2,3,4]
print(1 in num)  #returns True
print(a in num )  #returns false

    #not in
print(a not in num) #returns True
print(1 not in num) #returns False becuse the 1 is present in the num

    # Indentify operator-->
    #identity operators are used to check whether two variables refer to the same object in memory, not just whether they have equal values.
    #is-->Returns True if both variables point to the same object
a=1,2,3,4
b=a
print(a is b) #returns true becouse b is refe to the same object in memory

x=[1,2,3]
y=[1,2,3]
print(x is y)  #returns False becouse both have the same values but not refer for same object in the memory
print(x==y)  # look it is true but above is not

    # is not-->Returns True if both variables point to different objects
x=1,2,3
y=1,22,3
print(x is not y) #returns True becouse points the different

print(a is not b) #returns False becuse both are point to same objects


# 6) Bitwise Operators
 #Bitwise operators perform operations on binary representations of integers and  These operators are useful for low-level programming tasks like working with bits and bytes.

'''  Common Bitwise Operators:
&: Bitwise AND (sets each bit to 1 if both bits are 1).
|: Bitwise OR (sets each bit to 1 if one of the bits is 1).
^: Bitwise XOR (sets each bit to 1 if only one of the bits is 1).
~: Bitwise NOT (inverts all the bits).
<<: Left shift (shifts bits to the left by a specified number of positions).
>>: Right shift (shifts bits to the right by a specified number of positions).'''

a=21
b=12
print(a&b)  #returns 4 
print(a|b) #returns 29
