# Write a program that takes an age as input and prints:
# "You are an adult" if the age is 18 or older.
# "You are a minor" if the age is under 18.
# Modify the program to include:
# "You are a teenager" if the age is between 13 and 17.

age = int(input("How old are you?"))
if age>=22:
    print("You are an adult")
elif age>13 & age<=17:
    print("You are a teenager")
else:
    print("You are a minor")

