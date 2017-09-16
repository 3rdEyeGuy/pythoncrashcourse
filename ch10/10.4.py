with open('guest_book.txt', 'a') as file_object:
    print('\n' + 'Hello, please enter your name to check in: ')
    name = input()
    while name != 'exit':
        print('Have a most wonderful stay', name +'!')
        print('Thank you for checking in.')
        file_object.write(name + '\n')
        print('\n' + 'Hello, please enter your name to check in: ')
        name = input()
