"""
1. formatting strings
2. processing user input
"""
age = 26
name = "Vy"
# I'm 26

print("I'm", age)
print("I'm " + str(age))
print("I'm {}".format(age))
print(f"I'm {age}")

print('-' * 30)

# My name is Vy, I am 26
print("My name is", f"{name}, I am", age)
print("My name is " + str(name) + ", I am " + str(age))
print("My name is {0}, I am {1}".format(name, age))

# f-strings - f - format - fast
print(f"My name is {name}, I am {age}")
