

#EXTRA PRACTICE CHALLENGE

# 1️⃣ Take a number → print square & cube

num=float(input("enter value: "))
print("square value is: ",num**2)
print("cube value is: ", num**3)


# 2️⃣ Take total seconds → convert to minutes
sec=int(input("enter seconds: "))
print("minutes", sec//60)
print("remains", sec%60 , "seconds")

# 3️⃣ Take price & tax % → calculate final price
price=float(input("enter the price: "))
tax=float(input("enter the  tax percentage: "))
tax_amt=(price*tax)/100
print("total price is: ", price+tax_amt)

# 1️⃣ Area of Rectangle

# Take length and width → calculate area.
length=float(input("enter length in cm: "))
width=float(input("enter width in cm: "))
print("total area is: ", length*width, "cm")

# 2️⃣ Area of Circle

# Take radius → calculate area.
radius=float(input("enter radius in cm: "))
print(3.14*radius*radius)

#3️⃣ Convert Celsius to Fahrenheit
celcius=float(input("Enter celcius: "))
print((celcius*9/5)+32, "Fahrenheit")

# 4️⃣ Convert Kilometers to Meters
kilo=float(input("enter kilometers in km: "))
print(kilo*1000, "meters")

#5️⃣ Calculate Average of 5 Subjects
kannada=float(input("enter kannada marks: "))
english=float(input("enter english marks: "))
hindi=float(input("enter hindi marks: "))
social=float(input("enter social marks: "))
science=float(input("enter science marks: "))
total=(kannada+english+hindi+social+science)
print("your total marks is: ", total)
print("average is: ", total/5)

#6️⃣ Even or Odd (Using Modulus)

'''Take a number → print remainder when divided by 2.

(You don’t need if-else yet. Just show remainder.)'''
n=int(input("enter the number: "))
if n%2==0:
    print("entered number is even")
else:
    print("entered number is odd")

#7️⃣ Total Bill with GST
'''Take:
Product price
GST %

Print:
GST amount
Final bill'''

pr_price=float(input("enter product price: "))
gst=float(input("enter gst percentage: "))
gst_amt=(pr_price*gst)/100
print("gst amout is: ", gst_amt)
print("total bill is: ", pr_price+gst_amt)

'''8️⃣ Split Bill Among Friends

Take:

Total bill

Number of friends

Print how much each person should pay.'''

t_bill=float(input("enter total bill: "))
total_frd=float(input("enter total frieds: "))
print("separate amt for each is ",t_bill/total_frd)
'''9️⃣ Convert Minutes to Hours + Minutes

Example:
130 minutes → 2 hours 10 minutes

(Hint: use // and %)'''

min=int(input("enter the time in minutes: "))
hour=min//60
print("total time is", hour)
print("remaining time is: ", min%60, "minutes")

'''🔟 Swap Two Numbers (Without Third Variable)

Example:
x = 5
y = 10

Swap them using operators only.'''
x = 5
y = 10

x=x+y
y=x-y
x=x-y
print(x,y)

#using 3rd variable
a=5
b=10
temp=a
a=b
b=temp
print(a,b)

'''1️⃣1️⃣ BMI Calculator

Take:

Weight (kg)

Height (meters)'''

weight = float(input("Enter weight in kg: "))
height_cm = float(input("Enter height in cm: "))
height_m = height_cm / 100
bmii = weight / (height_m ** 2)
print("BMI is:", round(bmii, 2))

'''1️⃣2️⃣ Salary After Deduction

Take:

Basic salary

Tax %

PF %

Calculate final salary.'''
basic=float(input("enter your basic salary: "))
tax=float(input("enter tax percentage: "))
pf=float(input("enter the pf percentage: "))
taxamt=(basic*tax)/100
print("deducted tax amt: ", taxamt)
pfamt=(basic*pf)/100
print("deducted pf amt: ", pfamt)
remain_salary=basic-taxamt-pfamt
print("total salary after deduction: ", remain_salary)

'''1️⃣4️⃣ Convert Total Seconds to:

Hours

Minutes

Seconds

(Hint: multiple floor divisions + modulus)'''
seconds=int(input("Enter time in seconds: "))
hours=seconds//3600
remain_secs=seconds%3600
minutes=remain_secs//60
seconds=remain_secs%60
print(hours, "hours", minutes, "minutes", seconds, "seconds")


'''1️⃣5️⃣ EMI Calculator (Advanced Version)

Take:

Loan amount

Annual interest rate

Time in years

Calculate simple interest + total payable amount.'''

loan_amt=float(input("enter loan amout: "))
int_rate=float(input("enter interest rate: "))
time=float(input("enter time in years: "))
simple=(loan_amt*int_rate*time)/100
print(simple)
print("total payble amt is: ", loan_amt+simple)