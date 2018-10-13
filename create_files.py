# /usr/bin/env python
import os

# specify the start and end point of the files
n = 3
end = 55

print("Starting point:", "3")
# Just to create a bunch of exercise files.
while n < end:
    filename="ex" + str(n) + ".py"
    folder="exercise"
    file_path=os.path.join(folder, filename)
    create_file="touch " + file_path
    os.system(create_file)

    n += 1

print("The last file created : {0}".format(file_path))
