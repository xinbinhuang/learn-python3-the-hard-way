i = 0
numbers = []


def a_loop(n_loop=6, by=1):
    """A simple while loop adding number to a list"""

    global i, numbers

    while i < n_loop:
        print(f"At the top i is {i}")
        numbers.append(i)

        i = i + by
        print("Numbers now: ", numbers)
        print(f"At the bottom i is {i}")


a_loop(n_loop=10, by=2)
print("The numbers: ")

for num in numbers:
    print(num)
