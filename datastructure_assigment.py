cordinates = (10, 25, 23)
x, y, z = cordinates
print("x-cordinate:", x)
print("z-cordinate:", z)

student = {"name": "miracle"}
student["grade"] = "B"

print(student)

set1 = {1, 4, 5, 7}
set2 = {2, 4, 6, 7}

union = set1 | set2
intersection = set1 & set2
difference = set1 - set2
print(union)
print(intersection)
print(difference)


# Write a Python function called merge_lists that takes two lists as input and returns a new list
# containing all elements from both lists without duplicates.
def merge_lists(list1, list2):
    return list(set(list1 + list2))


first_list = [2, 4, 5, 7]
sec_list = [3, 5, 6, 5, 7]

print(merge_lists(first_list, sec_list))


#  Implement a function named find_max_min that takes a tuple of numbers as input and returns
# a tuple containing the maximum and minimum values in the tuple.
def find_max_min(tup):
    return (max(tup), min(tup))


odd = (4, 6, 8, 56)

print(find_max_min(odd))


# Create a Python function called count_words that takes a string as input and returns a
# dictionary containing the count of each word in the string.
def count_words(word):
    return {word: sum(1 for char in word)}


the_word = count_words(input("Enter a word"))
print(the_word)

# Write a function named remove_duplicates that takes a list as input and returns a new list
# containing only unique elements, preserving their original order.
def remove_duplicates(list):
    return set(list)


print(remove_duplicates([1, 3, 3, 4, 5, 6, 6]))

# Implement a generator expression to generate the squares of numbers from 1 to 10 lazily.
y = 1

while y <= 10:
    print(y*y)
    y = y+1
