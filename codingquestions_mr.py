# Question 1 
# Write a function to print "hello_USERNAME!" USERNAME is the input of the function. 

def hello_name(user_name):
    """Display simple user greeting"""
    print(f"hello_{user_name}!")


hello_name("USERNAME")

# Question 2
# Write a python function, first_odds that prints the odd numbers from 1-100 and returns nothing

def first_odds():
    """Display odd numbers from 1-100 and returns nothing"""
    for first_odd in range(1, 100):
        if first_odd % 2 != 0:
            print(first_odd, end="\n")


first_odds()

# Question 3
# Please write a Python function, max_num_in_list to return the max number of a given list.

def max_num_in_list(a_list):
    """Showcase the highest number from a list"""
    return max(a_list)

a_list = [2, 34, 101, -15, 4, 72, 23, 57, -45]
print(max_num_in_list(a_list)) 
 
 # Question 4
 #Write a function to return if the given year is a leap year. 
 # A leap year is divisible by 4, but not divisible by 100, unless it is also divisible by 400. The return should be boolean Type (true/false).

def is_leap_year(a_year):
    """Showcase a leap year through true or false statement"""
    if a_year % 4 == 0 or a_year % 100 != 0 and a_year % 400 == 0:
      return True
    if a_year % 4 == 0 and a_year % 100 == 0 and a_year % 400 == 0:
      return False


print(is_leap_year())


# Question 5
# Write a function to check to see if all numbers in list are consecutive numbers. 
# For example, [2,3,4,5,6,7] are consecutive numbers, but [1,2,4,5] are not consecutive numbers. 
# The return should be boolean Type.

def is_consecutive(a_list):
    """Sorting Consecutive Numbers"""
    consecutive_num = list(range(min(a_list), max(a_list)+1))
    sort_list = sorted(a_list)
    if sort_list == consecutive_num:
        return True
    else:
        return False


numbers = [2,3,4,5,6,7]
print(is_consecutive(numbers))
