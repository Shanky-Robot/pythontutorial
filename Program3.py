# String methods
# upper and lower strings

all_low = "there are no capital here. "
print(all_low.upper())
print(all_low)
all_up= "THIS IS SHOUTING TEXT."
print(all_up.lower())

# isupper ans islower gives boolean values

print(all_up.islower())
print(all_up.isupper())
#
# .isalpha() only for letters
# .isalnum() only for numbers and letters
# .isdecimal() only for numbers
# .isspace() only spaces
# .istitle() only titlecases
# non of them will work on empty strings

print("Batman123".isalpha())
print("Batman".isalnum())
print("123".isdecimal())
print(" ".isspace())
print("             ".isspace())
print("is not space".isspace())
print("is not a space"[2].isspace())
print("The Empire Strikes Back".istitle())
print("One Punch!!".istitle())
print("one punch man".title())

# .startswith() and .endswith() checks if the string starts or ends with the one mentioned , its case sensitive
print(all_low.startswith("there"))
print(all_low.startswith("There"))
print(all_up.endswith("."))

# .join() joins the string
print("".join(["one", "two", "three"]))
print(" ".join(["one", "two", "three"]))
print("|".join(["one", "two", "three"]))
print(" | ".join(["one", "two", "three"]))

# .split does opposite of join
print("Eggs, Milk, Bacon, Eggs".split())
print("Eggs, Milk, Bacon, Eggs".split(","))
print("Eggs, Milk, Bacon, Eggs".split(", "))

# Do all of this in a .py file in Pycharm:
#
# Create a variable called mixed_case and assign it the string "A Song of Ice and Fire"
#
# Use .isupper() to check if mixed_case is a string of all upper case letters.  print() the result.
#
# Use .islower() to check if mixed_case is a string of all lower case letters.  print() the result.
#
# Change all of the letters in mixed_case to upper case letters using .upper() and print() the result.
#
# Change all of the letters in mixed_case to lower case letters using .lower() and print() the result.
#
# Use the .istitle() method to check if mixed_case is title case and print the result.
#
# Create a variable called title_case and assign it the result of .title() being called on mixed_case.
#
# print() title_case
#
# Call startswith() on mixed_case with the letter mixed_case starts with as its argument.  print() the result.
#
# Call endswith() on mixed_case with the letter mixed_case ends with as its argument.  print() the result.
#
# Create a variable called words and assign it the result of split() being used on mixed_case.
#
# print the variable "words"
#
# Use the .join() method to join together all of the items in the list assigned to words as a single string.
# Use .isalpha() to check if the string is made up entirely of letters.  Finally, use print() to display the result.

mixed_case = "A Song of Ice and Fire"
print(mixed_case.isupper())
print(mixed_case.islower())
print(mixed_case.upper())
print(mixed_case.lower())
print(mixed_case.istitle())
title_case = mixed_case.title()
print(title_case)
print(mixed_case.startswith("A"))
print(mixed_case.endswith("e"))
words = mixed_case.split()
print(words)
print("".join(words).isalpha())

# .rjust() .ljust() justified

print("hello world".rjust(15))
print("hello world".ljust(15) + "four spaces later")
print("hello world".rjust(15, "*"))

# .center() fills on either side
print("Money".center(15, "$"))

# .strip() , .rstip() and .lstrip() removes spaces

print("juice, bread, cheese, beef, bread".rstrip(", bread"))
print("juice, bread, cheese, beef, bread".rstrip(", ed arb"))
print("juice, bread, cheese, beef, bread".lstrip("juice, "))
print("blueblueyellowblue".strip("eulb"))

# .replace() search and replace
print("Good Morning!".replace("Morning", "Afternoon"))

# string methods 2 exercises
# Do all of this in a .py file:
#
# Create a variable called the_string and assign it the string "North Dakota".
#
# Call .rjust() on the_string with 17 as its argument and print() the result.
#
# Call .ljust() on the_string with the arguments 17 and "*" then print() the result.
#
# Create a variable called center_plus and assign it the result of .center() being called on the_string with 16 and
# "+" as arguments.
#
# Use print() to display the string assigned to center_plus.
#
# Call .lstrip() on the_string to remove "North" then print() the result.
#
# Call .rstrip() on the_string with "+" as its argument and print() the result.
#
# Call .strip() on the_string with "+" as its argument and print() the result.
#
# Call .replace() on the_string and replace "North" with "South".  print() the result.

the_string = "North Dakota"
print(the_string.rjust(17))
print(the_string.ljust(17, "*"))
center_plus = the_string.center(16, "+")
print(center_plus)
print(the_string.lstrip("North"))
print(center_plus.rstrip("+"))
print(center_plus.strip("+"))
print(the_string.replace("North", "South"))

# len() lenght of strings

print(len("tree brisch lol words"))
print("antibodiesofcoronavirus"[7:20])
print(len("antibodiesofcoronavirus"[7:20]))


# Programming Challenge: String Reverser
# For this challenge, you will be writing a program which uses a for loop to reverse a string.
#
# Start by creating a variable and assigning it a string as user input using input().
#
# Use a for loop to reverse the string.  You will need to use range with all 3 inputs for this.  In addition,
# you should create a variable before the for loop and assign it an empty string.  The variable will be reassigned
# multiple times within the for loop and end up holding the new reversed string.
#
# Print the reversed string at the bottom of your program.

user_string = input("Please enter a string.")
reversed = ""

for item in range(len(user_string) - 1, -1, -1):
    reversed += user_string[item]

print(reversed)


# Programming Challenge: Word Counter For this programming challenge, write a program in a .py file which takes a
# string (you can assign the string to a variable or use input() to get a string from a user) and uses two print()
# statements to display a list of all of the words that the string contains as well as the number of words in the
# string.
#
# For example, if the program was used on the string "This is a string.", then the first print statement would
# display ['This', 'is', 'a', 'string'] and the second print statement would display 4.  Remember, to break up a
# string into that kind of a list, you would use the .split() method.
#
# Also, notice that there is no "." after "string" in the list displayed by the first print() statement:  For this
# program, you should get rid of everything from the list except numbers, letters, and spaces before using .split().
# That will remove all punctuation and odd characters from the string, including periods from acronyms and floats as
# well as escape sequences and apostrophes used in contractions.
#
# Since numbers are being kept, they will count as words.  So, if the string the program was being used on was "James
# Bond is 007.", then the number "007" would count as a word and the string would have 4 words total.
#
# You should test your program with many different strings.  However, the string that the solution code is being used
# on is the string below, which is a quote from the movie Forrest Gump.  This string has been assigned to a variable
# called str_1, so if you copy the code into your .py file, make sure to change the variable name to whatever you
# have been using.
#
# str_1 = "Anyway, like I was sayin', shrimp is the fruit of the sea. You can barbecue it, boil it, broil it, bake it, \
# saute it. Dey's uh, shrimp-kabobs, shrimp creole, shrimp gumbo. Pan fried, deep fried, stir-fried. There's pineapple \
# shrimp, lemon shrimp, coconut shrimp, pepper shrimp, shrimp soup, shrimp stew, shrimp salad, shrimp and potatoes, \
# shrimp burger, shrimp sandwich. That- that's about it."


str_1 = "Anyway, like I was sayin', shrimp is the fruit of the sea. You can barbecue it, boil it, broil it, bake it, \
saute it. Dey's uh, shrimp-kabobs, shrimp creole, shrimp gumbo. Pan fried, deep fried, stir-fried. There's pineapple \
shrimp, lemon shrimp, coconut shrimp, pepper shrimp, shrimp soup, shrimp stew, shrimp salad, shrimp and potatoes, \
shrimp burger, shrimp sandwich. That- that's about it."

spaces_and_letters = ""

# this for loop reduces the string to letters, numbers, and spaces
for char in str_1:
    if char.isalnum() or char.isspace():
        spaces_and_letters += char

words = spaces_and_letters.split()
number_of_words = len(words)

print(words)
print(number_of_words)

# format() concatonate and formats the strings

name = input("Whats your name ?")
age = input("How old are you ?")
employed = input("are you employed?")

print("Your name is " + name + " Your age is " + age + " Employed: " + employed)
print(" Your name: {}, Your age: {}, Employed: {}".format(name, age, employed))
