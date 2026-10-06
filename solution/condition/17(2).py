# Task 17: Grade Calculator
# Accept marks and calculate a grade. Reject marks outside the valid range.


marks = int (input("Enter Your Marks to Know Your Grade :- "))

if marks <= 100 and marks > 1:
    if marks > 90:
        print("Your grade is A+")
    elif marks > 80 :
        print("Your grade is A")
    elif marks > 70 :
        print("Your grade is B+")
    elif marks > 60 :
        print("Your grade is B")
    elif marks > 50 :
        print("Your grade is C+")
    elif marks >= 35 :
        print("Your grade is C")
    else :
        print("Your are Fail")
else :
    print("Please enter valid marks.")