with open('learning_python.txt') as file_object:
    print()
    for line in file_object:
        line = line.rstrip()
        print(line.replace('Python','C'))
    print()

