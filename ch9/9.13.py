from collections import OrderedDict

codingDict = OrderedDict()

codingDict["if"] = "Performs a loop \"if\" the statement is true."
codingDict["for"] = "Performs a loop a given amount of times."
codingDict["while"] = "Performs a loop an unknown amount of times until the loop statement is false."
codingDict["return"] = "Placed at the end of a function. Used to return a value\
 for the function called."
codingDict["print"] = "Prints a string literal."
codingDict[".py"] = "The file extension for a python program."
codingDict["dict()"] = "A method which creates a dictionary."
codingDict["list()"] = "A method which creates a sorted list."
codingDict["range()"] = "A method which creates a list from 0 to the highest value."
codingDict["len()"] = "A method which counts the amount of elements in a list."

for i in codingDict:
    print('\n'+i+':',codingDict[i])

print()
