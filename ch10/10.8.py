filenames = ['cats.txt','dogs.txt']

try:
    for filename in filenames:
        printFile(filename)
except:
    print("The file '"+ filename + "' is missing.")

def printFile(file_names):
    with open(file_names) as fObj:
        lines = fObj.readlines()
        for line in lines:
            print(line.rstrip())

