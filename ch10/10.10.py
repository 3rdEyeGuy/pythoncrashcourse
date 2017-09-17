"""Open a file and count the number of times the word "the" appears in the file"""

#prompt user for input
f_name = input("Enter the name of a file: ")
word = input("Enter the search word or phrase: ")

#exception block in case file is not found
try:
    with open(f_name) as f_obj:
        contents = f_obj.read()
        wordCt = contents.lower().count(word)
except:
    print("File was not found")

#prints word count
else:
    print("In the file '" + f_name + "', the word or phrase \"" + word + "\" appeared", wordCt, "times.")
