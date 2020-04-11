# Course session 5 to 8 udemy python tutorial
# comparator
print(5 > 2)
print(2 > 5)
print(5 >= 4.59)
print(3.3 <= 3.4)
print(7 == 8)
print("HEllo" == "world")
print("HELLO" == "hello")

#  boolean logic
print(4 > 2 and "word" == "word")
print(5 > 2 or "ME" == "Hello")
print(not "ME" == "Hello")

"""
# if else statement
 veg = input("Type the name of the Vegetable  ")


if veg == "carrot":
    print("the vegetable is CARROT")
else:
    print("teh vegetable is not CARROT")

# nested if else loop
gpa = float(input("WHat is your GPA? "))
inst_app = input("Whats your insitute? ")

if gpa >= 3.7:
    if inst_app == "Yes":
        print("You Qualify")
    else:
        print("You do not qualify")
else:
    print("You do not qualify")

"""

## Test 1

# Professor Fuentes teaches a Python class and uses the following grading scale for all of her exams. You work as a
# teacher's assistant and due to her busy schedule she has requested that you write a program which will determine
# the grades of the class's students.
#
# Her grading scale is as follows:
#
# A score of 90 or above is an A
#
# A score of 80 or above is a B
#
# A score of 70 or above is a C
#
# A score of 60 or above is a D
#
# A score any lower is an F
#
# For this exercise, start by creating a variable and assigning that variable a student's score as an integer using
# input().
#
# Then, using nested if and else statements and the following set of rules, determine and then display the student's
# grade along with their score using print().
#
# If the student's score is greater than or equal to 90, then the student will receive an A grade.
#
# Otherwise, if the student's score is greater than or equal to 80, then the student will receive an B grade.
#
# Otherwise, if the student's score is greater than or equal to 70, then the student will receive an C grade.
#
# Otherwise, if the student's score is greater than or equal to 60, then the student will receive an D grade.
#
# Otherwise, the student will receive an F grade.
#
# Make sure to run your program multiple times and test it with values for each 5 of the different grades to make
# sure that the correct output is displayed for any value entered as a student's score.

"""
grades = int(input("What is your grade out of 100? : "))

if grades >= 90:
    print("You get " + str(grades) + " which is A grade")
else:
    if grades >= 80:
        print("You get " + str(grades) + " which is B grade")
    else:
        if grades >= 70:
            print("You get " + str(grades) + " which is C grade")
        else:
            if grades >= 60:
                print("You get " + str(grades) + " which is D grade")
            else:
                print("You get" + str(grades) + "which is F grade")

"""

# else if statement elif
"""
user_num = int(input("how old are you ?  "))

if user_num < 0:
    print("you are not born yet")
elif user_num <= 10:
    print("you are born")
elif user_num > 10:
    print("you will survive")
elif user_num > 100:
    print("you are dead")

"""

# Programming Challenge: Roman Numeral Equivalent For this exercise, start by creating a variable and assigning it a
# randomly generated integer between and inclusive of both 1 and 10.
#
# Then, using your knowledge of if, elif, and else statements, create a program which prints the roman numeral
# equivalent of the randomly generated number.
#
# For example, if the randomly generated integer was 9, then the program would say that the roman numeral equivalent
# of 9 is IX in the output.

"""
from random import randint

one_to_ten = randint(1, 10)

if one_to_ten == 1:
    print("The roman numeral equivalent of " + str(one_to_ten) + " is I.")
elif one_to_ten == 2:
    print("The roman numeral equivalent of " + str(one_to_ten) + " is II.")
elif one_to_ten == 3:
    print("The roman numeral equivalent of " + str(one_to_ten) + " is III.")
elif one_to_ten == 4:
    print("The roman numeral equivalent of " + str(one_to_ten) + " is IV.")
elif one_to_ten == 5:
    print("The roman numeral equivalent of " + str(one_to_ten) + " is V.")
elif one_to_ten == 6:
    print("The roman numeral equivalent of " + str(one_to_ten) + " is VI.")
elif one_to_ten == 7:
    print("The roman numeral equivalent of " + str(one_to_ten) + " is VII.")
elif one_to_ten == 8:
    print("The roman numeral equivalent of " + str(one_to_ten) + " is VIII.")
elif one_to_ten == 9:
    print("The roman numeral equivalent of " + str(one_to_ten) + " is IX.")
else:
    print("The roman numeral equivalent of " + str(one_to_ten) + " is X.")
    
"""

## Truthy and falsey values
"""
string_1 = input("Enter something  "
                 "")

# if string_1 != "":
if string_1:
    print("you typed " + str(string_1))
else:
    print("You didn't type shit")


print(bool(0))
print(bool(1.32))
print(bool(""))
print(bool("YOLO"))

"""

# while loop

counter = 0

while counter < 5:
    print("something " + str(counter))
    counter += 1

# Programming Challenge: Sum of Numbers From A Positive Integer
# Write a program which gets a positive integer from a user using input() and assigns it to a variable.
#
# The program should then use a while loop to get the sum of all of the integers from the integer that was entered by
# the user down to 1.  For example, if the integer entered by the user was 6, the while loop would find the sum of 6,
# 5, 4, 3, 2, and 1, which is 21.
#
# At the bottom of your program create two print statements.  One will display the user entered integer and the other
# will display the sum found by the while loop.

"""
# pos_int is a variable which holds a user entered integer.
pos_int = int(input("Please enter a positive integer."))
# This variable stores the initial value of pos_int before it is used in the loop so
# that later it can be used to display pos_int's initial value in the output.
int_init = pos_int
# This is a variable which will be used to hold the sum of all the integers from pos_int.
summed = 0
# The while loop will run while pos_int's stored integer value is greater than 0
while pos_int > 0:
    # This is the equivalent of summed = summed + pos_int
    # In other words: new value of summed = old value of summed + new value of pos_int
    summed += pos_int
    # This will decrement pos_int so that pos_int will eventually equal 0 and the while
    # loop will stop running its code.
    pos_int -= 1

print(int_init)  # displays the initial value of pos_int
print(summed)  # displays the sum of integers from pos_int
"""

## For Loop

word = "house"

for letter in word:
    print(letter)

# Programming Challenge: Find The Number of Characters in A String
# In a .py file, write a program which calculates the number of characters in a string.
#
# The string should be entered using input() and assigned to a variable.
#
# Use print() twice at the end of your program.  The first print() will print the string that the user entered and
# the second print() will display the number of characters in the string.  For example, if the user entered the
# string "hello world", the number of characters would be 11.


"""
user_str = input("Please enter a string.")

count = 0  # This variable will be used to hold the number of characters in the string.
# This for loop adds 1 to count for each character in user_str.
for char in user_str:
    count += 1

print(user_str)
print(count)

"""

# range() its its own data type
# one = range(5)

# for num in one:
#    print(num)

# input_1 = range(5, 10)

# for num in input_1:
#    print(num)


# input_2 = range(1, 20, 3)

input_2 = range(20, 1, -3)

for num in input_2:
    print(num)

# Programming Challenge: Fizz Buzz
# Write a program that prints the integers 1 through 50 using a loop.
#
# However, for numbers which are multiples of both 3 and 5 print “FizzBuzz” in the output. For numbers which are
# multiples of 3 but not 5 print “Fizz” instead of the number and for the numbers that are multiples of 5 but not 3
# print “Buzz” instead of the number.
#
# All of the remaining numbers which are not multiples of 3 or 5 should just be printed as themselves.

for num in range(1, 51):
    # If num is divisible by both 3 and 5, "FizzBuzz" will be printed.
    if num % 3 == 0 and num % 5 == 0:
        print("FizzBuzz")
    # If num is only divisible by 3, "Fizz" will be printed.
    elif num % 3 == 0:
        print("Fizz")
    # If num is only divisible by 5, "Buzz" will be printed.
    elif num % 5 == 0:
        print("Buzz")
    # num itself will be printed in all other cases.
    else:
        print(num)


# Programming Challenge: Factorial
# Create a function which takes one positive integer as its input and returns its factorial.
#
# To make sure that your function works correctly, you should call it with the inputs 3, 4, and 5 and print what is
# returned by those calls.  For those inputs, you should get 6, 24, and 120, respectively.

# The argument fac_num's name is short for factorial number.

def factorial(fac_num):
    # The local variable returned will be used in the for loop used to calculate fac_num's
    # factorial. To do this, it will be multiplied by decrementing values of
    # fac_num. Since it will be multiplied, it was given the initial value of 1.
    returned = 1
    # By the end of this for loop, returned will have been reassigned fac_num's factorial.
    for item in range(fac_num, 1, -1):
        returned *= item

    # returns returned, which now holds the value of fac_num's factorial
    return returned


print(factorial(3))  # 6
print(factorial(4))  # 24
print(factorial(5))  # 120
