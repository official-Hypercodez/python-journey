# Variables and Data Types

# A variable is a name given to a memory location in program.

name = 'Sachin'
age = 17
price = 25.23

print(name)
print(age)
print(price)

print("my name is : ",name)
print("my age is : ",age)

# Rules for identifiers

'''
1 - Identifiers can be combination of uppercase and lowercase letters, digits or an underscore(_).
    So myVariable,variable_1,variable_for_print all are valid python identifiers.
2 - An identifier can not start with digit, So while variable1 is valid, 1variable is not valid.
3 - We can't use special symbols like !,#,%,$,@ etc in out identifier.
4 - Identifier can be of any length.
'''

# Data Types

# Integers
# String
# Float
# Boolean
# None

print(type(name))
print(type(age))
print(type(price))

# String (str)

name1='sachin'
name2="sachin"
name3='''sachin'''

print(name1)
print(type(name1))
print(name2)
print(type(name2))
print(name3)
print(type(name3))

# Integer (int)

age=17
print(age)
print(type(age))

# Float

price1=99.99
print(price1)
print(type(price1))

# Boolean (bool)

old = False
print(old)
print(type(old))

new = True
print(new)
print(type(new))

# None

a=None
print(a)
print(type(a))

# Keywords

# keywords are reserved words in python

# python is case sensitive 
 
# A and a are different (A != a)

'''
and         else        in          return       

as          except      is          True

assert      finally     lambda      try

break       False       nonlocal    with

class       for         None        while

continue    from        not         yield

def         global      or

del         if          pass

elif        import      raise

'''

# Types of Operators

# An operator is a symbol that performs a certain operation between operands.

# Arithmetic operators (+, -, *, /, %, **)

a=5
b=3

print(a + b)
print(a - b)
print(a * b) 
print(a / b) 
print(a % b) # remainder
print(a ** b)  # a^b

# Relational / Comparison Operators (==, !=, >, <, >=, <=)

a=50
b=20

print(a == b)   #False
print(a != b)   #True
print(a > b)    #True
print(a < b)    #False
print(a >= b)   #True
print(a <= b)   #False


# Assignment Operators (=,+=,-=,*=,/=,%=,**=)

a=10
print(a)
a = a+10
print(a)
a +=10
print(a)
a-=10
print(a)
a/=10
print(a)
a**=10
print(a)
a*=10
print(a)
a%=10
print(a)


# Logical Operators (not, and, or)
x=50
y=30
print(not (x>y))
print(not (x<y))

val1=True
val2=True
val3=False

print(val1 and val2)
print(val1 and val3)
print(not (val1 and val3))
print(val1 or val2)
print(val1 or val3)
print( not (val1 or val3))

# Type Conversion

a,b=10,'20'
# sum = a+b error 

b=int(b)
sum=a+b
print(sum)

a=float(a)
print(a)

a=str(a)

print(type(a))

name ='sachin'
# name =float(name) error

# Input in Python

# input() statement is used to accept values (using keyboard) from user

input() # result for input() is always a str

a1=input()
print(a1)
print(type(a1))

name4=input('Enter your name : ')
print(name4)

# Ptactice Questions

# write a program to input 2 numbers & print their sum
print('Sum of two numbers')
n1=int(input('Enter your 1st number : '))
n2=int(input('Enter your 2nd number : '))

sum=n1+n2
print(n1,' + ',n2,' = ',sum)

# WAP to input side of a square & print its area.
print('Area of a square')
s1=float(input('Enter square side : '))
print(s1*s1)

# WAP to input 2 floating point numbers & print their average.
print('Average of two numbers')
num1=float(input('Enter your first number : '))
num2=float(input('Enter your second number : '))

print((num1 + num2) / 2)