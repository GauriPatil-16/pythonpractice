#Task 19: Login Validation
#Create a simple username/password login with a limited number of attempts.

correctuser= "gauri"
correctpass = 11123

attempts = 3
username =input("enter your valid username :- ")
password =int(input("enter your valid password :-"))

if username ==correctuser  and password == correctpass :
  print("password is correct")
else:
    attempts= attempts - 1
    print("wrong password")
    print("try again :-", attempts)

    username =input("enter your valid username :- ")
    password =int(input("enter your valid password :-"))

    if username ==correctuser  and password == correctpass :
        print("password is correct")
    else:
        attempts= attempts - 1
        print("wrong password")
        print("try again :- ",attempts)
        username =input("enter your valid username :- ")
        password =int(input("enter your valid password :-"))

        if username ==correctuser  and password == correctpass :
            print("password is correct")
        else:
            attempts= attempts - 1
            print("wrong password")
            print("limit is over ")






