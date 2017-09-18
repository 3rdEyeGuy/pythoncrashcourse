import json

#read favorite number from file
fileName = 'favNum.json'
with open(fileName) as f_obj:
    favNum = json.load(f_obj)

#print favorite number
print("Your favorite number is:", str(favNum))
