# Integer (int)
age = 21
count = 100
print(age)      # 21
print(type(age))  # <class 'int'>

# Float (float)

price = 99.99
pi = 3.14
print(price)
print(type(price))  # <class 'float'>

# String (str)

name = "Danny"
message = 'Hello World'
print(name)
print(type(name))  # <class 'str'>

# Boolean (bool)

is_student = True
is_logged_in = False
print(is_student)
print(type(is_student))  # <class 'bool'>

# List (list)  Ordered and mutable
fruits = ["apple", "banana", "mango"]
fruits.append("orange")  # add item
print(fruits)
print(type(fruits))  # <class 'list'>

# Tuple (tuple) Ordered but immutable
coordinates = (10, 20)
print(coordinates)
print(type(coordinates))  # <class 'tuple'>

#Function (def)
# Reusable block of code
def greet():
    print("Hello!")
greet()   # calling the function