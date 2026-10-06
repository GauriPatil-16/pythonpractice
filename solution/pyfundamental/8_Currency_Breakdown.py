#Currency Breakdown
#Accept an amount and determine the number of notes required for selected denominations.

amount = int(input("enter the amount "))
notes_500 = amount // 500
remaining1 = amount % 500

notes_200 = remaining1 // 200
remaining2 = remaining1 % 200

notes_100 = remaining2 // 100
remaining3 = remaining2 % 100

notes_50 = remaining3 // 50
remaining4 = remaining3 % 50

notes_20 = remaining4 // 20
remaining5 = remaining4 % 20

notes_10 = remaining5 // 10
remaining6 = remaining5 % 10

notes_5 = remaining6 // 5
remaining7 = remaining6 % 5

notes_2 = remaining7 // 2
remaining8 = remaining7 % 2

notes_1 = remaining8 // 1
remaining9 = remaining8 % 1

print(amount)
print("500rs note :-",notes_500)
print("200rs note :-",notes_200)
print("100rs note :-",notes_100)
print("50rs note :-",notes_50)
print("20rs note :-",notes_20)
print("10rs note :-",notes_10)
print("5rs note :-",notes_5)
print("2rs note :-",notes_2)
print("1rs note :-",notes_1)




