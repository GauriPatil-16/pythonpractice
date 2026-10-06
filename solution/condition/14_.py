#Task 14: Largest of Three
#Find the largest of three numbers using conditional statements.

num_1 = int(input("enter the num_1 :- "))
num_2 = int(input("enter the num_2 :- "))

num_3 = int(input("enter the num_3 :- "))

if num_1 > num_2  and num_1 > num_3 :
    print("num1 is greater")
elif num_2 > num_3 and num_1 > num_3:
    print("num2 is greater")
else:
    print("num3 is greater")