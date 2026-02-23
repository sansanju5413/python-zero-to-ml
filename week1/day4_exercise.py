'''
1️⃣ Store 5 Marks in a List

Take 5 subject marks from user
Store in list
Print:

Total

Average
'''
marks=[]
kannada=int(input("enter kannada marks: "))
marks.append(kannada)
english=int(input("enter english marks: "))
marks.append(english)
hindi=int(input("enter hindi marks: "))
marks.append(hindi)
social=int(input("enter social marks: "))
marks.append(social)
science=int(input("enter science marks: "))
marks.append(science)
print(marks)
print("total obtained marks is: ", sum(marks))
print("total average is: ", sum(marks)/len(marks))


'''
2️⃣ Find Maximum Number in a List

Take 5 numbers → store in list
Print maximum using:
'''
num=[]
for i in range(5):
    number=int(input("enter the number: "))
    num.append(number)
    print(num)

print(max(num))


'''3️⃣ Count Even Numbers in a List

Take 5 numbers → store in list
Count how many are even.

(Hint: loop + modulus)'''
val=[]
for i in range(5):
    inp=int(input("enter the value: "))
    val.append(inp)
    print(val)
count=0

for i in val:
    if i%2==0:
        count+=1
print("even number count:", count)