# /usr/bin/env python
import os


def confirm_create():
    msg = f"Create files from `ex{start}.py` to `ex{end}.py`? ([yes]/no) :"
    yes = input(msg).lower().strip()

    if yes in ['yes', 'y', '']:
        yes = True
    elif yes in ['no', 'n']:
        yes = False
    else:
        yes = confirm_create()

    return yes


# specify the start and end point of the files
start = n = 1
end = 52

# Ask for user input to confirm create files
yes = confirm_create()
while n <= end and yes:
    filename = f"ex{n}.py"
    folder = "exercise"
    file_path = os.path.join(folder, filename)
    create_file = "touch " + file_path
    if os.path.isfile(file_path):
        pass
    else:
        os.system(create_file)

    n += 1

try:
    print('Job finished. Bye~')
except NameError:
    print('No files were created. Bye~')
