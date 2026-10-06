#Task 7: Time Converter
#Convert a number of seconds into hours, minutes, and remaining seconds.
seconds = int(input("enter th hour"))
hours = seconds // 3600
remaining = seconds % 3600

minutes = remaining // 60
seconds = remaining % 60

print("Hours :", hours, "Minutes :", minutes,"Seconds :", seconds)
