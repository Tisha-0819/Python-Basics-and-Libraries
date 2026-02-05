# Task 2:-Use NumPy to create an array of numbers and string and perform 
# basic operations(sum, mean, median, max, min, split, append, insert, concatenate, sort)

import numpy as np
# Creating arrays using NumPy
number_array = np.array([10, 20, 18, 12, 50])
string_array = np.array(['Tisha', 'is', 'learning', 'NumPy'])

# Basic operations on number array
sum = np.sum(number_array)
mean = np.mean(number_array)
median = np.median(number_array)
max = np.max(number_array)
min = np.min(number_array)
print("number_array operations: ")
print("Sum:", sum)
print("Mean:", mean)
print("Median:", median)
print("Max:", max)
print("Min:", min)

# Basic operations on string array
split_string = np.char.split(string_array[2])  # Splitting the third element
appended_array = np.append(string_array, 'library')  # Appending a new string
inserted_array = np.insert(string_array, 1, 'really')  # Inserting a string at index 1
concatenated_array = np.char.add(string_array, ' is great!')  # Concatenating a string to each element
sorted_array = np.sort(number_array)  # Sorting the string array
print("\nstring_array operations: ")
print("Split:", split_string)
print("Appended Array:", appended_array)
print("Inserted Array:", inserted_array)
print("Concatenated Array:", concatenated_array)
print("Sorted Array:", sorted_array)
print("\n")
