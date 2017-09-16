print("Hello, what is your name?")
name = input()

with open('guest.txt', 'w') as file_object:
    file_object.write(name)
