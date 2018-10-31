# /usr/bin/env python
import os

# specify the start and end point of the files
n = 1
end = 56

print(f"Starting point: {n}")
# Just to create a bunch of exercise files.
while n < end:
    filename = f"ex{n}.py"
    folder = "exercise"
    file_path = os.path.join(folder, filename)

    if not os.stat(file_path).st_size:
        create_file = "touch " + file_path
        os.system(create_file)

    n += 1

print("The last file created : {0}".format(file_path))
