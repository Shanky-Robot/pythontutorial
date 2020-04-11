# commenting
# section 1 to section 4 of course python -Udemy
"""
print('Hello World 1st Python Program 2.8.2020 - 2:51')


a = 5
b = 4
c = a + b
print(c)

add = 4 + 5
subtract = 5 - 2
divide = 7 / 2
multiply = 5 * 3

exponent = 4 ** 4
floor_division = 16 // 5  # 3
modulo = 7 % 3  # 1

add_assign = 5
add_assign += 7
print(add_assign)

lol = True
print(lol)
print((9 - 7) * 2 ** 3 + 10 % 6 // -1 * 1 * 2 - 1)

print(1.23 + 2.80)
print((123 + 280) / 100)
print(round((1.23 + 2.80), 52))
print(10.9 + 211.05)

# A customer of a grocery store is purchasing 6 items. The names and prices of the items are as follows:
#
# Penne 16 oz Pack of 12 - $16.68
#
# Arrabiata Pasta Sauce 24 oz - $6.98
#
# Bag of 20 Organic Garlic Cloves - $16.78
#
# Italian Seasoning 1.5 oz Bottle - $15.26
#
# Artisan Baguettes Twin Pack - $3.00
#
# 12 oz Bag of Meatballs - $4.39
#
# In a .py file, write a program which calculates the subtotal of all 6 of these items using an expression.  The subtotal is just the sum of all of their prices.
#
# Use print() to display the result of the expression.

penne = 16.68
sause = 6.98
garlic = 16.78
seasoning = 15.26
baguettes = 3.00
meatballs = 4.39
print(round((penne + sause + garlic + seasoning + baguettes + meatballs), 2))

##
ex_1 = 'this is a string.'
ex_2 = "this is also a string"
print(ex_2[2])  # this will access lower case "i" as it is indexed as 2.. the index starts with 0
print("apple"[4])  # now this will index lower case "e" as index no. 4
# python slicing
print(ex_1[:3])
print(ex_1[2:10])

print("pecan" + " " + "pie")

concatenated = "R2" + "-" + "D2"

to_slice = "Just do it!"
print(to_slice[10])  # prints "!"
print(to_slice[5:7])  # prints "do"
print(to_slice[8:])  # prints "it!"
print(to_slice[:4])  # prints "Just"
print("Don't " + to_slice[5:])  # prints "Don't do it!"

# type() detects type of variable
# str() converts things into strings

# escape sequence \t - tab size space

print("this\tis\ta\tlot\tof\tspace")

# \n new line charater

print("Hello \n World")

# \ and \

print(" when it is \' party time\' bitch")
print("*******\n ***** \n  ***  \n   *   ")


# name = input("what is your name ?")
# print("your name is  " + name + ".")
# print(type(name))

# monty python quest test

# name = input("What is your name?")
# quest = input("What is your quest?")
# color = input("What is your favorite color?")

# print("So your name is " + name + ", your quest is " + quest + ", and your favorite color is " + color + ".")

# int() and float()
# userin = input("please enter fav no.")
# print(userin)
# print(type(userin))

# int exercise In a Python file, use input() to ask the user to enter an integer that 10 will be added to.  Assign
# what they type to a variable. print() the sum of the integer they entered and 10.

# solution 1
# use_int = int(input("Please enter an integer."))

# print(use_int + 10)


# solution 2

# use_int = input("Please enter an integer.")

# print(int(use_int) + 10)

# functions

def print_lol():
    print("this")
    print("is")
    print("epic")
    print("lol.")


print_lol()
print_lol()
print_lol()


def function():
    print(2 + 2)


function()


def functiontest(parameter):
    print(parameter + 2)


functiontest(8)

first_str = "The number "


def function_name(p1, p2, p3):
    print(p1 + str(p2) + p3)


function_name(first_str, 5, " is an integer")


def deault_exp(num1=7, num2=8):
    print(num1 * num2)


deault_exp()  # this has default value 8 and 7
deault_exp(2, 10)  # this has new values 2 and 10


def default_exp(num1=7, num2=8):
    return num1 * num2


product = default_exp()
print(product)

# The formula for converting from degrees Celsius to degrees Fahrenheit is as follows:
#
# F = 1.8 * C + 32
#
# Where F is the Fahrenheit temperature and C is the Celsius temperature.
#
# In a .py file, create a variable and assign it an integer representing a celsius temperature that is entered as
# user input().  input()'s message should prompt the user to enter an integer value.
#
# For this programming challenge, you will then write a function called fahrenheit that takes in an integer
# representing a Celsius temperature as its argument.  The function will return the Fahrenheit equivalent temperature
# of that argument to 1 place after the decimal.
#
# At the end of your program, display the Fahrenheit equivalent in a print statement message formatted like so:  "The
# Fahrenheit equivalent of [user entered integer] degrees Celsius is [number returned by function]".
#
# To make sure that the function works, run your program multiple times and call the function on different user
# entered integer values both negative and positive.

celsius = int(input("Please enter an integer value for degrees celsius. "))


def fahrenheit(cel):
    # To avoid the approximation error that would occur if the float 1.8 was used in the calculation, 1.8 * 10 is used
    # instead, resulting in the integer 18.  To balance this out, 32 is also multiplied by 10 to get 320.  After the
    # calculations in the parentheses are finished, the result is divided by 10, which gives the correct Fahrenheit
    # temperature.
    return (18 * cel + 320) / 10


print("The Fahrenheit equivalent of " + str(celsius) + " degrees Celsius is " + str(fahrenheit(celsius)) + ".")

# new solution with round

celsius = int(input("Please enter an integer value for degrees celsius. "))


def fahrenheit(cel):
    # The second argument of round() is 1 since we only want the Fahrenheit temperature to be displayed with 1 number
    # after the decimal point
    return round((1.8 * cel + 32), 1)


print("The Fahrenheit equivalent of " + str(celsius) + " degrees Celsius is " + str(fahrenheit(celsius)) + ".")

# module import

import random

print(random.randint(1, 10))

# function import

from random import randint

print(randint(10, 20))

# universal import

from random import *

print(random())

# Programming Challenge: Miles Per Gallon

# For this exercise, you will create a program that approximates the number of miles per gallon that a car gets.
#
# In a .py file, create two variables, one which will hold a randomly generated integer between 10 and 25 (inclusive
# of both 10 and 25), and another which will hold a randomly generated integer between and inclusive of 200 and 400.
# The first variable represents the number of gallons of gas that the car's fuel tank holds. The second variable
# represents the miles that the car can travel on a full tank before needing a refuel.
#
# Using the formula miles per gallon (MPG) = miles driven/gallons used, calculate the car's MPG and display it in the
# output using print().  Use floor division instead of regular division for this calculation to get an integer
# instead of a float.  This will give a realistic approximation of miles per gallon even though floats such as 19.8
# round down a large amount when using floor division since sometimes, car manufacturers sometimes exaggerate miles
# per gallon.  In addition, display the values held in the variables you created for gallons of gas in the car's fuel
# tank and miles it can travel on a full tank with two different print statements.

from random import randint

# generates random integer between and inclusive of 10 and 25 to represent gas in the car's fuel tank
fuel = randint(10, 25)
# generates random integer between and inclusive of 200 and 400 to represent miles the car can go without refueling
miles = randint(200, 400)
# calculates and displays the MPG of the car assuming car manufacturers overestimates in their claims
print("The car can travel " + str(miles // fuel) + " miles per gallon.")
# displays the number of gallons of fuel that the car's fuel tank can hold
print("The car's fuel tank can hold " + str(fuel) + " gallons.")
# displays the number of miles that the car can travel on a full tank
print("The car can travel " + str(miles) + " miles on a full tank.")

# Variable scope

example = "Hello world"


def loc_ex():
    example = "this is a string"
    return example


print(example)
print(loc_ex())


# local variable name and global variable name

def loc_ex1():
    fruit = "pear"
    print(fruit)


def loc_ex2():
    fruit = "banana"
    print(fruit)


fruit = "mango"
loc_ex1()
loc_ex2()
print(fruit)


def loc_glob():
    global fruit
    fruit = "watermelon"
    print(fruit)


loc_glob()
print(fruit)

"""