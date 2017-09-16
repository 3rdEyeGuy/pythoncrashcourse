#name of file to be appended to
filename = 'iLoveCode.txt'

#opens file, prompts question and assigns response to reason
with open(filename,'a') as file_object: 
    print('\n'+'Why do you love coding?')
    reason = input()

    #exit loop by typing 'exit'
    #loops question, assigns answer and writes answer to file
    while reason != 'exit':
        file_object.write(reason + '\n')
        print('\n'+'Why do you love coding?')
        reason = input()
