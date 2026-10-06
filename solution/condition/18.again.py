# Task 18: Electricity Bill
# Calculate an electricity bill using slab-based rates.

units = int(input("How much units consumed :- "))

if units <= 100 :
    bill = units * 5
    print("Your bill is ",bill)
elif units <= 300 :
    bill = (100 * 5) + ((units - 100)*7)
    print("Your bill is ",bill)
else :
    bill = (100 * 5) + ((units - 100)*7) + ((units - 300)*9)
    print("Your bill is ",bill)