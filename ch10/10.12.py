import json

def readNum():
    #read favorite number from file
    fileName = 'favNum.json'
    with open(fileName) as f_obj:
        favNum = json.load(f_obj)

    return favNum

def askNum():
    #Prompt user for favorite number
    favNum = input("What is your favorite number? ")

    #store fav. number in a file
    fileName = 'favNum.json'
    with open(fileName, 'w') as f_obj:
        json.dump(favNum, f_obj)

    return favNum

try:
    favNum = readNum()
except:
    favNum = askNum()
    #print favorite number
    print("Your favorite number is:", str(favNum))

else:
    #print favorite number
    print("Your favorite number is:", str(favNum))
