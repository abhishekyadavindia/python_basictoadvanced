# Print Statement in Python
print("HelloWorld")
# Single Line Comment in Python
'''
Multiline
Comment
in
Python
'''
# Variables in Python
'''
Rules to Declare Variable in Python:
A variable name must start with a letter or the underscore character.
A variable name cannot start with a number.
A variable name can only contain alpha-numeric characters and underscores. (A-z, 0-9, and _ )
Variable names are case-sensitive (age, Age and AGE are three different variables).
'''
a = 5
b = 6
print(a+b)
# Assign Values to Multiple Variables
x, y, z = "Orange", "Banana", "Pineapple"
j = k = l ="orange"
# Data Types in Python
# Text Type: str
# Numeric Types: int, float, complex
# Sequence Types: list, tuple, range
# Mapping Type: dict
# Set Types: set, frozenset
# Boolean Type: bool
# Binary Type: bytes, bytearray, memoryview
# str - String Type
# Declaration of String in Variable:
string = "This is String"
# int-Integer Data Type
# All Negative Numbers, Positive Numbers with 0 is called Integers. For Example, -1,0,1,2,3,4..etc.
# Declaration of Integer in Variable:
integer = 1
# float - Floating Point Number
# All Integers with decimal point and fractional numbers are called Floating Point Numbers. For Example, 2.545, 65.454, ... etc.
# Declaration of Floating Point Numbers in Variable
float_num = 2.4545454
# complex - Complex Numbers
# All Imaginary Numbers are called Complex Numbers.
# It has jth series in mathematical representation. So, in Variable's numbers we define j after that number to define it as complex.
# Declaration of Complex Numbers in Variable
complex_num2 = 1245j
# Type Method in Python
# Type tells datatype of the variable or parameter passed.
print(type(string))
# Type Casting in Python
# Type Casting means changing datatype manually.
var = 12
print(type(var))
# If we want to type caste integer to string or float then,
var = float(var)
print(type(var))
var = str(var)
print(type(var))
# If we want to change float to string
float_no = 1654.59568
print(type(float_no))
float_no = str(float_no)
print(type(float_no))
# If we have to change string to integer or float
string_int = "12"
print(type(string_int))
string_float = "12.5364"
print(type(string_float))
string_int = int(string_int)
print(type(string_int))
string_float = float(string_float)
print(type(string_float))
# Strings and its Functions/Methods
# As above we have seen double quotes denotes string in variable declaration.
# Example of Single Line String
string_single_line_example = "This is single line string"
print(type(string_single_line_example))
# Example of Multiline String
# Use Three Double Quotes.
string_multi_line_example1 = """This
                                is
                                multiline 
                                string"""
print(type(string_multi_line_example1))
# Or, You can also use Three Single Quotes
string_multi_line_example2 = '''This
                                is
                                multiline
                                string'''
print(type(string_multi_line_example2))
# Strings are Arrays and can be used as Lists
# In Python, Strings are Arrays so you can use methods which are used in details in Lists in Strings like indexing and all things related to index.
# In Strings letters have index.
# Slicing - Strings
string_slice = "slice string"
print(string_slice[2:5])
# About this you can read in more details in Lists.
# Length
# If we have to print length of any string, integer, float, or any other data type. We use len()
string_length = "length of string"
print(len(string_length))
# String Methods
# The strip() method removes any whitespace from the beginning or the end
string_whitespace = "    HelloWorld    "
print(string_whitespace)
print(string_whitespace.strip())
# The lower() method returns the string in lower case.
string_lower = "HELLo"
print(string_lower.lower())
# The upper() method returns the string in upper case.
string_upper = "hello"
print(string_upper.upper())
# The replace() method replaces a string with another string.
# Syntax:replace(old key, new key)
string_replace = "hatty"
string_replace = string_replace.replace("t", "r")
print(string_replace)
# The split() method splits the string into substrings if it finds instances of the separator.
c = "Hello, World!"
c = c.split(",")
print(c)
# Outputs: ['Hello', ' World!']
# Check String
string_var = "this is string"
check_exists = "string" in string_var
check_not_exists = "that" in string_var
print(check_exists)
print(check_not_exists)
# Returns True if Exists and Returns False if dosen't
# String Concatenation
string1 = "hello"
string2 = "world"
concatenate = string1 + string2
print(concatenate)
# Note that Strings and Numbers cannot be concatenated like this.
# We can concatenate strings also using format method.
# The format() method takes the passed arguments, formats them, and places them in the string where the placeholders {}.
name1 = "harry"
name2 = "harish"
concate = "My name is {} and my friend name is {}".format(name1, name2)
print(concate)
# format works on index. Placeholders {} are by default {0}, {1}, {2}... and takes parameters of format. If we write format in indexes it has index like, format({0}, {1}, {2}...) and it displays where ever this index is defined. For Example, if we write variables same and want to change it using index in placeholders then,
concate_same = "My name is {0} and my friend name is {1}".format(name1, name2)
print(concate_same)
# This is same as concate but if you change parameters in placeholder.
concate_different = "My name is {1} and my friend name is {0}".format(name1, name2)
print(concate_different)
# Now you would be able to see difference between them. {}--> by default takes 0, 1, 2, ...
# To change them you have to define index.
# There is one more way also to do this using f-string which is introduced from Python-3.6 onwards.
concate_f = f"My name is {name1} and my friend name is {name2}"
print(concate_f)
# Taking Input from User
# input_var = input("Enter the Number")
# print(type(input_var))
# Here you would see all entries in this is of str type, to take entry of number and do operations, we have to type caste it to integer.
# input_var = int(input_var)
# Escape Characters
# What if we say you to print double quotes inside a string.
# You can write-->
# variable = "String notation in Python is "string""
# print(variable)
# But if you would try it you would get error.
# To be safe from error we use Escape Character.
# Here we can use \ to avoid error, like this.
variable = "String Notation  in Python is \"string\""
print(variable)
# Escape Character is also used to pproduce new line.
new_character = "helloworld\n"
print(new_character)
# There are many other escape character like
'''
\' - For Single Quote
\\ For Backslash
\n For New Line
\r For Carriage Run - You can use between string to take string after this character below that line(works like Enter key in your Keyboard).
\t For Tab - Works like Tab Button in your Keyboard(creates whitespace where ever used).
'''
# Booleans in Python
# In programming you often need to know if an expression is True or False.
# You can evaluate any expression in Python, and get one of two answers, True or False.
# When you compare two values, the expression is evaluated and Python returns the Boolean answer.
print(10>9)
print(10==12)
print(bool("Hello"))
print(bool(15))
# It would return true when you would enter valid strings, float values, integers, etc.
# Most Values are True but some values are false like:
print(bool(False))  # If statement itself is given false.
print(bool(None))   # If statement has None.
print(bool(0))      # If entered 0.
print(bool(""))     # If entered empty string.
print(bool())       # If entered empty tuple.
print(bool([]))     # If enetred empty list.
print(bool({}))     # If entered empty set.
# Operators in Python
# There are Total Seven Operators in Python:
'''
1. Arithmetic Operators
2. Assignment Operators
3. Comparison Operators
4. Logical Operators
5. Identity Operators
6. Membership Operators
7. Biwise Operators
'''
# Arithmetic Operators
# There are Seven Types of Arithmetic Operators:
'''
Operator            Name
+                  Addition 
-                 Subtraction
*                 Multiplication
/                   Division
%                   Modulus
**                Exponentiation
//                Floor Division
'''
num1 = 3
num2 = 2
# Addition Operator
print(num1+num2)
# Subtraction Operator
print(num1-num2)
# Multiplication Operator
print(num1*num2)
# Division Operator
print(num1/num2)
# Modulus Operator - Prints the remainder after dividing given number
print(num1%num2)
# Exponentiation Operator - Raises the Power
print(num1**num2)
# Floor Division Operator - Divides given and gives integer value(also if float exist)
print(num1//num2)
# Assignment Operators
'''
For any integer a
Operators           Use             Equal to
+=                  x+=a            x = x + a
-=                  x-=a            x = x - a
*=                  x*=a            x = x * a
/=                  x/=a            x = x / a
%=                  x%=a            x = x % a
//=                 x//=a           x = x // a
**=                 x**=a           x = x ** a
'''
# Comparison Operators
'''
Operator                Name
==                     Equal to
!=                    Not Equal to
>                     Greater than
<                      Less than
>=                Greater than or equal to
<=                  Less than or equal to
This all operators are widely used in boolean, conditionals, loops, and functions.
'''
# Logical Operators
# Logical operators are used to combine conditional statements.
'''
Operator            Description
and     Returns True if both statements are true.
or      Returns True if one of the statements is true
not     Reverse the result, returns False if the result is true.
'''
'''
Example of Logical Operators
x < 5 and  x < 10
x < 5 or x < 4
not(x < 5 and x < 10)
'''
# list - List
# A list is a collection which is ordered and changeable.
# Declaration of List in Variable
fruits = ["apple", "banana", "pineapple"]
# Printing Lists and its Components
print(fruits) # Printing List
# We can Access one of item using indexing in Python
# Indexing in Python starts from 0 and onwards
# So first apple in list has index 0 , banana has index of 1, etc.
# So to print banana you can write
print(fruits[1])
# Syntax: print(list variable name[index])
# Negative Indexing in Python
# if any one writes
print(fruits[-1])
# Then he is writing index from left side. For example, in our case this would result in pineapple(because in negative indexing it dosen't starts from zero)
# So, Negative indexing means beginning from the end, -1 refers to the last item, -2 refers to the second last item etc.
# Range of Indexes
# When we have to type list(or this is applicable for string also) range we can define range of index.
# In range defining, index starts from 0 but you have to specify last as 1 more, because it takes one null list.
# So to print whole list fruits we have write first index 0 but last would not be 2 but 3. 
print(fruits[0:3])
# Syntax to Print List from beginning to end: print(name of list variable[0:last index + 1])
# Printing Beginning to that index
# To print list from starting to any index, we can write:
print(fruits[:3])
# Printing from Index to Last
# Like Above we can print list from any index to end of list.
print(fruits[0:])
# Range of Negative Indexes
print(fruits[-3:-1])
# It dosen't prints first value of your list.
# Other Operations are like above.
# Changing Values of List
# List values can be changed.
fruits[1] = "cherry"
print(fruits)
# List Length/String Length can be found using len
print(len(fruits))
print(len(string))
# Adding Values in List
fruits.append("orange")
print(fruits)
# Adding Values in List at any Index
fruits.insert(1, "papaya")
# Syntax: name of list variable.insert(index, "changing name")
# Removing Item from List
fruits.remove("papaya")
# Removing Last Item in List(also can be used as remove function if first parameter is entered as index)
fruits.pop()
print(fruits)
# Empty the List
fruits.clear()
# Copy lists
integers = [1,2,3,4,5]
list_string = ["int", "float", "string"]
integers_copy1 = integers.copy()
print(integers_copy1)
# Join Two Lists
list_add = integers + list_string
print(list_add)
# Function to Join Lists
integers.extend(list_string)
# Another Way to Build list
# You can use list construct for building list.
list_construct = list(("apple", "cherry", "banana"))
# Some other methods for lists are remove(), reverse(), sort()
# tuple - Tuples
# A tuple is a collection which is ordered and unchangeable. In Python tuples are written with round brackets.
# Some methods of lists are used in tuples also like accessing tuples data, range of indexes, etc.
# But to add or delete tuples we have to use different methods.
tuple_example = ("apple", "banana", "cherry")
print(tuple_example)
# Create Tuple with One Item
tuple_one = ("apple",)
# In the case comma is not written in parantheses after only one value then it is not tuple.
# Join Two Tuples
tuple_add = ("string", "integer", "float")
tuple_added = tuple_add + tuple_one
print(tuple_added)
# Delete Tuple
# You can not edit tuple items but you can delete the whole tuple using del
del tuple_one
# Tuple Constructor
tuple_construct = tuple(("abhishek", "banana"))
print(tuple_construct)
# Python has two built-in functions to use on tuples-count() and index()
# set - Sets
# A set is a collection which is unordered and unindexed. In Python sets are written with curly brackets.
set_create = {"apple", "papaya", "pineapple"}
# Add Items in Set
# Add method used above is used here.
# Add Multiple Items in Set
set_create.update(["cherry", "banana"])
# Check if banana is present in Set
print("banana" in set_create)
# Remove Item
set_create.remove("pineapple")
# Or
set_create.discard("banana")
# If item does not exist discard dosen't gives error.
# Join Two Sets
set_data = {"integer", "float", "string"}
set_join = set_create.union(set_data)
print(set_join)
# Or you can use Update method
set_create.update(set_data)
# Set Constructor
set_construct = set(("apple", "banana", "pineapple"))
# Some Methods for Set are difference(), difference_update(), intersection(), intersection_update(), isdisjoint(), issubset, issuperset(), symmetric_difference, symmetric_difference_update.
#dict - Dictionary
# A dictionary is a collection which is unordered, changeable and indexed. In Python, dictionaries are written with curly brackets, and they have keys and values.
Employee = {
    "name": "Harish",
    "year": 2005,
    "company":"Google"
}
print(Employee)
# Accessing Items
Employee_item = Employee["name"]
print(Employee_item)
# Or you can use get method
Employee.get("year")
# Change Values in Dictionary
Employee["year"] = 1995
print(Employee.get("year"))
# Adding Items in Dictionary
Employee["newyear"] = 1990
print(Employee.get("newyear"))
print(Employee)
# Removing Items
del Employee["newyear"]
# del can delete whole dictionary too.
# Copy Dictionary
Employee_Copy = Employee.copy()
# Clear Dictionary - Empty your Dictionary
Employee_Copy.clear()
# Delete Dictionary
del Employee_Copy
# Nested Dictionaries
# A dictionary can also contain many dictionaries, this is called nested dictionaries.
Employee = {
   "Employee1": { 
       "name":"harry",
        "salary":45000
},
    "Employee2": {
        "name":"harish",
        "salary":20000
}
}
print(Employee)
# Dictionary Constructor
# note that keywords are not string literals
# note the use of equals rather than colon for the assignment
Dict_construct = dict(name="harry", salary="45000")
print(type(Dict_construct))
print(Dict_construct)
# Conditionals - If and Else Statements
# All Logical Operators are used in If-Else Statements.
# Indentation
'''
Python relies on indentation (whitespace at the beginning of a line) to define scope in the code. Other programming languages often use curly-brackets for this purpose.
'''
# It means
# if(a>45):
# print("helloworld")
# would give error.
# but
# if(a>45):
#   print("helloworld")
# This would not give error.
# Syntax Of If-Conditional
# if(condition):
#   statement
# Syntax of Else-Conditional
# else:
#   statement
# Example:
a = 45
if (a>25):
    print("Number is greater than 25")
else:
    print("Number is less than 25")
# elif Conditional
# Elif runs after if statement and wherever finds result breaks to run other elif statements. But If you right many if statements, all would run and your program would be heavy.
age = 25
if age>18:
    print("You are Adult.")
elif age == 25:
    print("your age is 25")
else:
    print("Your age is unknown")
# Short Hand If
no1 = 12
no2 = 13
if no2>no1: print("no2 is greater than no1")
# Short Hand If..Else
print("no1 is less than no2") if no2>no1 else print("no2 is less than no1")
# This technique is known as Ternary Operators also.
# And in Conditionals - Logical Operators
# The and keyword is a logical operator, and is used to combine conditional statements.
no3 = 45
if no3>no2 and no1<no2:
    print("no3 is larger number")
else:
    print("no1 is larger number")
# Or in Conditionals - Logical Operator
# The or keyword is a logical operator, and is used to combine conditional statements.
if no3>no2 or no2<no1:
    print("helloworld")
else:
    print("I don't know")
# Nested If
# You can have if statements inside if statements, this is called nested if statements.
x = 41

if x > 10:
  print("Above ten,")
  if x > 20:
    print("and also above 20!")
  else:
    print("but not above 20.")
# The Pass Statement
# if statements cannot be empty, but if you for some reason have an if statement with no content, put in the pass statement to avoid getting an error.
a_num = 33
b_num = 200

if b_num > a_num:
  pass
# Loops
'''
If we have to automate something we use Loops.
Python has two primitive loop commands:
1. While Loop
2. For Loop
'''
# While Loop
# With the while loop we can execute a set of statements as long as a condition is true.
i = 0
while i<10:
    print(i)
    i += 1 # Equal to i = i + 1
# Automate List Components Printing using While Loop
list_loop = ["while", "for", "loop"]
index = 0
while index<3:
    print(list_loop[index])
    index += 1
# Note: If index or increment or decrement variable is not defined the loop would go forever. And it would be Infinite Loop.
# Break Statement
# With the break statement we can stop the loop even if the while condition is true.
i = 0
while i<100:
    print(i)
    i += 1
    if i==10:
        break
# Continue Statement
# With the continue statement we can stop the current iteration, and continue with the next.
i = 0
while i<6:
    i += 1
    if i == 3:
        print(i)
# Else Statement in While Loop
# With the else statement we can run a block of code once when the condition no longer is true.
i = 1
while i<6:
    print(i)
    i += 1
else:
    print("i is no more now.")
# For Loop
# Print Numbers from 1 to 10 using for-loop
for i in range(1,11):
    print(i)
# range() is used widely in for loop for printing numbers.
# Automating List in For Loop
for i in list_loop:
    print(i)
# Looping through a String
for x in "tata":
    print(x)
# This prints its all alphabets line-by-line(this works becuase we know that string in python works like an array).
# Continue and Break statements which are used in while loop are used also used in for loop, using same way.
# Nested Loops
# A nested loop is a loop inside a loop.
# The "inner loop" will be executed one time for each iteration of the "outer loop".
adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
  for y in fruits:
    print(x, y)
# Pass Statement in Loops
# for loops cannot be empty, but if you for some reason have a for loop with no content, put in the pass statement to avoid getting an error.
for x in [0, 1, 2]:
  pass
# ----------------------------------------------
# Functions in Python
# Creating a Function in Python
def function_name():
    print("helloworld")
# Calling a Function
# If you build a function it dosen't prints statements written under it.
# To print the function we have to call function, like this.
function_name()
# Basics of Arguments in Functions
def function(string):
    print("this is " + string)
function("string")
# Add Function
def function_add(a, b):
    print(a+b)
function_add(2, 3)
# Now you can see it works very well, but if we want to do out of function , some other arthmetic operations, we can not do it.
# For doing it we use return.
def function_add_return(c, d):
    e = c+d
    return(e)
var = function_add_return(5, 4) * 2 
print(var)
# Now Your Basics of Python Programming is completed, now go and open advanced_py.py.
# The End.
