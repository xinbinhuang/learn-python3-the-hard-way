# assign variable with integer
types_of_people = 10
# assign a string with f-string and variable {types_of_people}
x = f"There are {types_of_people} types of people."

# assign variables with strings
binary = "binary"
do_not = "don't"
# assign a string with f-string and variables {binary} and {do_not}
y = f"Those who know {binary} and those who {do_not}."

# print out two string variables
print(x)
print(y)

# print out a new string with f-string and variables {x} and {y}
print(f"I said: {x}")
print(f"I also said: '{y}'")

# assign boolean: False to variable
hilarious = False
# assign a string to a variable
joke_evaluation = "Isn't that joke so funny?! {}"

# print out the joke_evaluation string with `.format` with variable {hilarious}
print(joke_evaluation. format(hilarious))

# assign strings to two variables
w = "This is the left side of..."
e = "a string with a right side."

# print out the concatenation of two strings
print(w + e)
