# tuples are imutable but list not

# 4 built-in data types in Python used to store collections of data, they are List, Set, and Dictionary, and Tuple.


# List is a collection which is ordered and changeable. Allows duplicate members.
# Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
# Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
# Dictionary is a collection which is ordered** and changeable. No duplicate members.

thistuple = ("apple", "banana", "cherry", "apple")
print(thistuple)

print(thistuple[0])

print(len(thistuple))

# allow duplicate values

# To create a tuple with only one item, you have to add a comma after the item

thistuple = ("apple",)