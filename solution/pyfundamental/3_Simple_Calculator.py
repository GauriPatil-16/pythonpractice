#Task 3: Simple Calculator
#Accept two numbers and display addition, subtraction, multiplication, division, floor division, modulus, and power.

num_1 = int(input("enter first number :- "))
num_2 = int(input("enter second number :- "))
operator = input("Enter operator (+, -, *, /,//,%,^): ")

match operator:
    case "+":
        print("add:-",num_1 + num_2)
    case "-":
        print("sub:-",num_1 - num_2)
    case "*":
        print("mul :-",num_1*num_2)
    case "/":
        print("div :-",num_1/num_2 )
    case "//":
        print("floor :-" ,num_1//num_2)
    case "%":
        print("module :-" ,num_1%num_2)
    case "**":
        print("power :-" ,num_1**num_2)
    case _:
        print("Invalid operation")