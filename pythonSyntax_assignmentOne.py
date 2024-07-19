"""#1.Showcase Your Dance Moves!
#Task 1: Code Correction Below is a piece of Python code with incorrect indentation. Your task is to correct it.

weather = "sunny"

if weather == "sunny":
  print("Wear sunglasses!")
else:
  print("Take an umbrella!")

#Task 2: Your Mood Today Ask the user how they feel today. 

# If they say "happy", print "That's great to hear!", and if they say "sad", print "I hope your day gets better!".
# Ensure your if statement is properly indented. 
# HINT: Use the input() function to ask the user how they feel! 

x = str(input("How do you feel?" ))

if x == "happy":
  print("That's great to hear!")
else:
  print("I hope your day gets better!")

#2. Python Naming Convention Practice

#Objective: 

#The aim of this assignment is to understand and apply Python's naming conventions, particularly for variables and constants.
#Task 1: Code Correction
#You have been given a piece of code with several variable and constant names that don't follow the Python naming convention.
#Your task is to correct them:

Pi_value = 3.14
userAge = 25
user_location = "New York"
MAXLIMIT = 1000

#Updated Python's naming conventions

pi_value = 3.14
a = type(pi_value)

user_age = 25
b = type(user_age)

userLocation = "New York"
c = userLocation

maxlimit = 1000
d = type(maxlimit)

print(a, b, c, d)

#3. Arithmetic Operations in Daily Life
#Objective: 
# The aim of this assignment is to get familiarized with basic arithmetic operations and understand how they can be applied in everyday situations.

#Task 1: Grocery Store Math
#Calculate the total cost of three items you'd commonly find in a grocery store, given their individual prices. For example, what would be the cost of bread, peanut butter, and jelly be? Prices don't need to be realistic!

tofu = 2.49
miso = 3.99
green_onions = 0.78

total_cost = tofu + miso + green_onions
print(total_cost)

#Task 2: Bank Interest 
# If you have a savings account with a particular initial amount and a fixed yearly interest rate, calculate the total amount in your account after a year. 
# So if you had $10,000 at a 7% interest write code that would tell us the amount at the end of the year. 
# For the example the expected outcome would be $10,700."""


p = 10000
r = .07

yearly_return = p * r
print(int(yearly_return + p))