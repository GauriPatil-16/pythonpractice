#Grade Calculator
#Accept marks and calculate a grade. Reject marks outside the valid range.
 

marks = int(input("enter the marks :- "))


if marks > 100:
    print("marks is invalid")
elif marks >= 80 :
    print("a+")
elif marks >= 70:
    print("a")
elif marks >= 60:
    print("b+")
elif marks >=50:
    print("b")
elif marks < 0:
    print("not valid ")

else:
    print("fail")