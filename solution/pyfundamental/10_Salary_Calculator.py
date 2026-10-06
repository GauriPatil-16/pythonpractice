#Task 10: Salary Calculator
#Accept basic salary, allowance percentage, and deduction percentage and calculate net salary.


allowance_percentage = int(input("enter the amount"))
deduction_percetntage= float (input("enter the pertage"))

net_salary1=allowance_percentage + deduction_percetntage - deduction_percetntage
net_salary2=allowance_percentage/100
net_salary3=allowance_percentage * deduction_percetntage / 100
print(net_salary3)

