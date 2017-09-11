with open("learning_python.txt") as file_object:
    content = file_object.read()

    print('\n' + "Reading in entire file")
    print(content)

with open("learning_python.txt") as file_object:
    print("Loop over lines")
    for line in file_object:
        print(line.rstrip())

    print()

with open("learning_python.txt") as file_object:
    print("Loop over list")
    lines = file_object.readlines()
    for line in lines:
        print(line.rstrip())
    print()
