"""Opens files and reads their contents"""

#Function to open and print files
def printFile(file_name):
    #Exception block
    try:
        with open(file_name) as fObj:
            lines = fObj.readlines()
            for line in lines:
                print(line.rstrip())
    except:
        print("The file '"+ file_name + "' is missing.")

#loop to use above function to print the files' contents.
filenames = ['cats.txt','dogs.txt']
for filename in filenames:
    print(filename + ':')
    printFile(filename)
