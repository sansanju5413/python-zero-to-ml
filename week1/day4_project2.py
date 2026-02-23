'''
Personal Expense Analyzer (Basic Version)
📌 Problem Statement

Build a program that:

Takes expenses for:

Food

Travel

Shopping

Rent

Other

Store them in a list.

Calculate and print:

Total expense

Average expense

Highest expense

Lowest expense

Check if total expense is greater than 10,000
'''
categories=["food", "travel", "shop", "rent", "other"]
expenses=[]
food=float(input("enter food expenses: "))
expenses.append(food)
travel=float(input("enter travel expenses: "))
expenses.append(travel)
shop=float(input("enter shopping expenses: "))
expenses.append(shop)
rent=float(input("enter rent expenses: "))
expenses.append(rent)
other=float(input("enter other expenses: "))
expenses.append(other)
print(expenses)

total=sum(expenses)
print("total expenses is: ", total)
print("average expenses is: ", total/len(expenses))
max_index=expenses.index(max(expenses))
min_index=expenses.index(min(expenses))
print("highest expenses is: ", max(expenses) , "at", categories[max_index])
print("lowest expenses is: ", min(expenses) , "at", categories[min_index])

if total>10000:
    print("total expenses is more than 10000: ")
else:
    print("not more than 10000")
