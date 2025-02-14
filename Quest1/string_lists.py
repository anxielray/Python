#  implement a function that reverses a string
# Lists comprehension is a concise way to create lists in Python.
# It allows you to generate lists by iterating over an existing list or range.
# The syntax is [expression for item in iterable if condition].

def reverse_string(s):
    return s[::-1]


if __name__ == "__main__":
    str = input("Enter a string: ")
    
    if str == None:
        print("No string provided")
    else:
        print(reverse_string(str))


# Regular for loop vs List comprehension
numbers = [1, 2, 3, 4, 5]

# Regular way to [populate a list]
squares = []
for n in numbers:
    squares.append(n ** 2)

# List comprehension way to [populate a list]
# add the square of each number in the list(numbers) to the list squares
squares = [n ** 2 for n in numbers]

# With condition
even_squares = [n ** 2 for n in numbers if n % 2 == 0]

# More examples
names = ['anxiel', 'brown', 'vashney']
# conversion of a string to uppercase
upper_names = [name.upper() for name in names]  # ['ANXIEL', 'BROWN', 'VASHNEY']

# Nested list comprehension
matrix = [[1, 2, 3], [4, 5, 6]]
flattened = [num for row in matrix for num in row]  # [1, 2, 3, 4, 5, 6]


# =====================String methods=====================================
text = "  Hello, World!  "

# Case manipulation
print(text.upper())       # "  HELLO, WORLD!  " converts every character to uppercase
print(text.lower())       # "  hello, world!  " converts every character to lowercase
print(text.title())       # "  Hello, World!  " converts the first character of each word to uppercase
print(text.capitalize())  # "  Hello, world!  " converts the first character of the string to uppercase

# Whitespace removal
print(text.strip())      # "Hello, World!" removes whitespace from the leading and trailing of the string
print(text.lstrip())     # "Hello, World!  " removes whitespace from the leading of the string
print(text.rstrip())     # "  Hello, World!" removes whitespace from the trailing of the string

# Splitting and joining
sentence = "Python is awesome"
words = sentence.split()  # ['Python', 'is', 'awesome'] splits the string into a list of words, splits by space by default, but a delimeter can be passed.
print("-".join(words))   # "Python-is-awesome" joins the list of words into a string with a separator

# Finding and replacing
text = "Hello, World!"
print(text.find("World"))    # 7 (index where "World" starts)
print(text.replace("World", "Python"))  # "Hello, Python!"

# Checking string properties
print("123".isdigit())   # True: checks for a string that is convertible to an integer
print("abc".isalpha())   # True: checks for a string that is alphabetic
print("abc123".isalnum()) # True: checks for a string that is alphanumeric

# String formatting
name = "Alice"
age = 25

# f-strings (Python 3.6+)
print(f"My name is {name} and I'm {age} years old") # Combining a string and a variable in the same string

# format() method
print("My name is {} and I'm {} years old".format(name, age)) # Using the format() method to insert variables into a string. Sometimes the curlybraces are passed with indices

# % operator (older style)
print("My name is %s and I'm %d years old" % (name, age)) # Using the % operator to insert variables into a string

# Slicing strings
text = "Python"
print(text[0:2])    # "Py"
print(text[2:])     # "thon"
print(text[::-1])   # "nohtyP" (reverse) this is a common way to reverse a string

# Practical examples combining both concepts
text = "python programming"

# List comprehension with string manipulation
vowels = [char for char in text if char in 'aeiou']  # ['o', 'o', 'a', 'i']

# Split and join with list comprehension
words = text.split()
capitalized = ' '.join([word.capitalize() for word in words])  # "Python Programming"

# Finding all indices of a character
indices = [i for i, char in enumerate(text) if char == 'p']  # [0, 7]

