import json

#Prompt user for favorite number
favNum = input("What is your favorite number? ")

#store fav. number in a file
fileName = 'favNum.json'
with open(fileName, 'w') as f_obj:
    json.dump(favNum, f_obj)

