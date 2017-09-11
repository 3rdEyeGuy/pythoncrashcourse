with open("learning_python.txt") as file_object:
    lines = file_object.readlines()

    print()

    for line in lines:
        print(line.rstrip())

    print()

with open("learning_python.txt") as file_object:
    for line in file_object:
        print(line.rstrip())

    print()

with open("learning_python.txt") as file_object:
    strings = ''
    for line in lines:
        strings += line.rstrip()

    for sentance in range(len(strings)):
        print(strings[sentance])
    print(len(strings))
