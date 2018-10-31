print("How old are you?", end='')
age = input()
print("How tall are you?", end=' ')
height = input()
print("How much do you weigh?", end=' ')
weight = input()

print(f"So, you're {age} old, {height} tall and {weight} heavy.", end="\n\n")


# which is equivalent to :

print("Which is equivalent to `input(\"prompt\")``")
age = input("How old are you:")
height = input("How tall are you:")
weight = input("How much do you weight")
print(f"So, you're {age} old, {height} tall and {weight} heavy.")
