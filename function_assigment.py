# This code creates a multiplication table
# Implement a program that generates a multiplication table from 1 to 12 based on user input using nested loops.
for i in range(1, 13):
    for j in range(1, 13):
        print(i * j, end="\t")
    print()


# Define a Python function called calculate_area_rectangle. This function should take the length and width of a rectangle as input parameters and return the area of the rectangle.
def area(length, width):
    return length * width


result = area(5, 2)
print(result)

# Create a Python script that prompts the user to enter their age and gender. If the age is greater than or equal to 18 and the gender is "male", print "You are a man"; if the age is greater than or equal to 18 and the gender is "female", print "You are a woman"; otherwise, print "You are a minor".

age = int(input("Please enter your age"))
gender = (input("Please input your gender"))

if age >= 18 and gender == "Male" or gender == "male":
    print("You are a man")
elif age >= 18 and gender == "Female" or gender == "female":
    print("You are a woman")
else:
    print("You are a minor")



# Create a Python function named check_prime that determines whether a given positive integer is a prime number. The function should take an integer num as input and return True if it is a prime number, and False otherwise

def check_prime(num):
    if num <= 1:
        return False
    if num == 2:
        return True
    if num % 2 == 0:
        return False
    max_divisor = int(num ** 0.5) + 1
    for d in range(3, max_divisor, 2):
        if num % d == 0:
            return False
    return True


test1 = check_prime(int(input("enter your number")))
print(test1)


# Develop a Python function called count_vowels that counts the number of vowels (a, e, i, o, u) in a given string. The function should take a string text as input and return the count of vowelsDevelop a Python function called count_vowels that counts the number of vowels (a, e, i, o, u) in a given string. The function should take a string text as input and return the count of vowels.
def count_vowels(word):
    vowels = "aeiouAEIOU"
    return sum(1 for char in word if char in vowels)


test = count_vowels(input("enter a word"))
print(test)


# Write a Python function named reverse_string that reverses a given string. The function should take a string text as input and return the reversed string.
def reverse_string(s):
    return s[::-1]


print(reverse_string(input('enter your string')))
