#Task 9: Simple Interest
#Accept principal, rate, and time and calculate simple interest and total amount.

Accept_principal = float(input("enter the principle :- "))
rate  = float(input("enter the rate :- "))
time  = float(input("enter the time :- "))

total_amount= (Accept_principal*rate*time)/100
print(total_amount)
