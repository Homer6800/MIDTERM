#question 1
a = 6

a = a - 2

print(a*2)

a = a * 2

print(a+1)

a = a // 3

#question 2

print((3+10**2/2) or 70.0)

#question 3

import datetime

a = 3
b = 4
today = datetime.datetime.today()
day_of_week = today.weekday()
month_of_year = today.month
a = a + day_of_week
b += month_of_year

print(a)
print(b)
c = a + b
print(c)
d = "abc" * (c // 3)
print(d)

#question 4
def palindrome(word):
    return word == word[::-1]

# Test the function with provided numbers
numbers = [
    "2704702208931031198668911301398022074072",
    "7798338247658278460338648728567428338977",
    "0974101607733149676776769413377061014790",
    "4257304920394478392772938744930294037524"
]

for num in numbers:
    if palindrome(num):
        print(f"{num} is a palindrome.")
    else:
        print(f"{num} is NOT a palindrome.")

#Question 5
text = """
In an uncertain world, unconventional plans may lead to unforeseen results. 
Some believe understanding the unknown can unlock many doors. 
An unclean plan, an unclear vision, or an unkind man can unsettle many. 
However, unity in action and unison in purpose can unfold an unimaginable plan. 
It's unusual for an unprepared person to understand the nuances of such undertakings.
"""

def find_un_an_occurrences(text):
    count = 0
    words = text.split()  # Split the text

    for word in words:
        word = word.lower().strip(".,!?")

        # Check if the word starts with 'un' and ends with 'an'
        if word.startswith('un') and word.endswith('an'):
            count += 1

    return count
number_of_occurrences = find_un_an_occurrences(text)
print(f"Number of occurrences: {number_of_occurrences)

#question 6
#Question 6


#Mutable objects are objects such as lists or dictionaries which can be altered and changed once created however
#unmutable objects are things such as strings which once created cannot be edited or changed such as strings which i will demonstrate

my_String = "Hello Homer"
print("Original String:", my_String)

# Trying to modify the string directly
try:
    my_String[0] = "hello John"
except TypeError as e:
    print("Error:", e)

# Correctly creating a new string and showing how to "modify" it
my_String = "hello john" + my_String[1:]
print("Modified String:", my_String)


#question 7
import random

# Create a list of random numbers
random_numbers = []
for i in range(10):
    random_numbers.append(random.randint(1, 100))

modified_numbers = []

for number in random_numbers:
    # Check if the number is even
    if number % 2 == 0:
        # Double the number and add it to the new list
        modified_numbers.append(number * 2)


# Print the original and modified lists for comparison
print("Original list:", random_numbers)
print("Modified list (doubled evens, removed odds):", modified_numbers)

#question 8

#Question 8

def is_valid_url(url):
    if url.startswith('http://') or url.startswith('https://'):
        if '.' in url:
            return True
    return False

# Example usage
print(is_valid_url('http://example.com'))  # Should return True
print(is_valid_url('https://example'))     # Should return False
print(is_valid_url('ftp://example.com'))   # Should return False

# we know that if a url does not include the http/https it will not be a functioning URL furthermore
#we also know if it dosent have . means it dosent have a domain controller relating to things such as .com or .co.uk
#or .ie and cant be a working URL either

#question 9

def days_since_my_birthday():

    birth_year = 2004


    # Replace 2023 with the current year in your use case
    current_year = 2023

    full_years_passed = current_year - birth_year - 1
    days_passed = full_years_passed * 365.25
    return int(days_passed)


# Call the function and print the result
print(f"Days passed since my birthday (excluding birth year and current year): {days_since_my_birthday()}")




