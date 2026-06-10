# Python First Programm

''' 
    In two different modes of Programming :
    1 - Interactive.
    2 - Script.

'''

# Interactive Mode Programming

# We can invoke a Python interpreter from command line by typing python at the command prompt as following −

# C:\Users\username>python
# Python 3.10.11 (tags/v3.10.11:7d4cc5a, Apr  5 2023, 00:38:17) [MSC v.1929 64 bit (AMD64)] on win32
# Type "help", "copyright", "credits" or "license" for more information.
# >>>

# >>> denotes a Python Command Prompt where we can type our commands 

# code

"""
>>> print('Hello world!')
Hello world!

"""

# Script Mode Programming

# How to write code in script mode 
# 1 -> download this file and rename it test.py or create new file called test.py
# 1.1 -> for new file type the following source code in a test.py file

print('Hello world!')

# save the changes

# 2 -> open command prompt
# C:\Users\username> 

# 3 -> locat current folder where our test.py file exist
# C:\Users\username\currentFolder> 

# 4 -> Now, let's try to run this program as follows
# command to run our program 'python filename.py'

# C:\Users\username\currentFolder> python test.py
# Hello world!     --> output


# Python Identifiers

'''
A Python identifier is a name used to identify a variable, function, class, module or other object.
An identifier starts with a letter A to Z or a to z or an underscore (_) followed by zero or more letters, underscores and digits (0 to 9).
'''


# Valid identifiers
name = 'Sachin'
lastName='Siddhartha'
full_name='Sachin Siddhartha'
_country = 'India'

print('Identifiers')
print(name)
print(lastName)
print(full_name)
print(_country)

# Invalid identifiers
# Python does not allow punctuation characters such as @, $, % within identifiers.

# $name = 'Sachin'
# last-name ='Siddhartha'
# full name = 'Sachin Siddhartha'
# @country = 'India'

# Python Reserved Words 

# we cannot use them as constant or variable or any other identifier names. 
# All the Python keywords contain lowercase letters only.

# and
# as
# assert
# break
# class
# continue
# def
# del
# elif
# else
# except
# False
# finally
# for
# from
# global
# if
# import
# in
# is
# lambda
# None
# nonlocal
# not
# or
# pass
# raise
# return
# True
# try
# while
# with
# yield

# Python Lines and Indentation

'''
The number of spaces in the indentation is variable, but all statements within the block
must be indented the same amount

'''

if True:
   print ("True")
else:
   print ("False")

if True:
    print('Answer')
    if True:
        print ("True")
else:
    print('Answer')
    print ("False")


# Python Multi-Line Statements

'''
Statements in Python typically end with a new line. Python does, however, allow 
the use of the line continuation character (\) to denote that the line should continue.
'''

total = 'Hello' + \
        'world' + \
        '!'

print(total)
# Helloworld!  --> output

# Quotations in Python

# Python accepts single ('), double (") and triple (''' or """) quotes to denote string literals, as long as the same type of quote starts and ends the string.

# The triple quotes are used to span the string across multiple lines.

word = 'word'
print (word)

sentence = "This is a sentence."
print (sentence)

paragraph = """This is a paragraph. It is
made up of multiple lines and sentences."""
print (paragraph)

'''
A hash sign (#) that is not inside a string literal begins a comment.
All characters after the # and up to the end of the physical line are part of the comment and the
Python interpreter ignores them.
'''

# First comment
print ("Hello, World!") # Second comment

name = "Madisetti" # This is again comment

# This is a comment.
# This is a comment, too.

# triple-quoted string is also ignored by Python interpreter and can be used as a multiline comments

'''
This is a multiline
comment.
'''