'''
🎓 Student Marks Analyzer
'''
'''📌 Problem Statement

Build a program that:

Takes marks for 5 subjects from the user.

Stores them in a list.

Then calculates and prints:

📊 Total marks

📈 Average marks

🔝 Highest mark

🔻 Lowest mark

🔢 Number of subjects

🟢 Count of even marks

🔴 Count of odd marks
'''
marks=[]
for subject in range(5):
    mark=int(input("enter the marks: "))
    marks.append(mark)

print("total marks: ", sum(marks))
print("average is: ", sum(marks)/len(marks))
print("highest marks is: ", max(marks))
print("lowest marks is: ", min(marks))
print("number of subjects: ", len(marks))
    
even_count=0
odd_count=0
for num in marks:
    if num%2==0:
        even_count+=1
    else:
        odd_count+=1
print("even marks is :", even_count)
print("count of odd number is: ", odd_count)


 
