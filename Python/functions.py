# Write a function multiply(a, b) that returns the product of two numbers.
# Write a function is_even(number) that checks if a number is even. It should return True if the number is even, and False otherwise.
# Write a function area_of_circle(radius) that calculates and returns the area of a circle. (Hint: Use pi * radius * radius)
# Write a function get_full_name(first_name, last_name) that returns the full name by combining the first and last name.
def multiply(a,b):
    print(a*b)
multiply(3,4)

def is_even(number):
    if(number%2==0):
        return True
    else:
        return False
check_number=is_even(4)
print(check_number)

def area_of_circle(radius):
    return 3.14*radius*radius
rad = area_of_circle(2)
print(rad)

def get_full_name(first_name,last_name):
    fullname = first_name+last_name
    return fullname

get_name = get_full_name("Muhammad","AnasKhan")
print(get_name)