name = 'Bin Huang'
age = 35 # a lie
height = 175 # cm
weight = 66 # kg
eyes = 'Brown'
teeth = 'White'
hair = 'Black'

# f-string: the 'f' of f"string" tells the string to be formatted
print(f"Let's talk about {name}.")
print(f"He's {height} cm tall.")
print(f"He's {weight} kg heavy.")
print("Actually that's not too heavy.")
print(f"He's got {eyes} eyes and {hair} hair.")
print(f"His teeth are usually {teeth} depending on the coffee.")

# this line is tricky, try to get it exactly right
total = age + height + weight
print(f"If I add {age}, {height}, and {weight} : I get {total}.")

height_inches = height * 0.393701 # cm to inches
weight_pounds = weight * 2.20462 # kg to pounds
print(f"Also, My height of {height} is equivalent to {height_inches};",
       "my weight of {weight} is equivalent to {weight_pounds}.")
