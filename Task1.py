# Task 1: Write a Python script and create 3 functions and 
# passing values in each other and show the result.

def function1(x):
    return x + 2

def function2(y):
    return y - 5

def function3(z):
    return z * 3

# Passing values in each other
result1 = function1(5)
result2 = function2(result1)
final_result = function3(result2)

print("Final Result:", final_result)