'''Day 3 Mini Project: Simple ATM Withdrawal Checker

Take:

Account balance

Withdrawal amount

Rules:

If withdrawal <= balance → allow

Else → insufficient balance'''


acc_balance=float(input("Enter your Accout Balance: "))
withdrawal=float(input("Enter the withdrawal amount: "))

if withdrawal<=acc_balance:
    print("transaction completed, Thank you.")
    print("Remaining balance is: ", acc_balance-withdrawal)
else:
    print("insufficient balance, Try again.")