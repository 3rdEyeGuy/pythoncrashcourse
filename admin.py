class Privileges():
    def __init__(self):
        self.privileges = ['adding posts','deleting posts','banning users']

    def show_privileges(self):
        print('An administrator\'s privileges include:')
        for i in range(len(self.privileges)):
            if self.privileges[i] == self.privileges[len(self.privileges) - 1]:
                print('and', self.privileges[i] + '.')
            else: print(self.privileges[i] + ',')

class Admin(User):
    def __init__(self, first_name, last_name,age,gender):
        super().__init__(first_name,last_name,age,gender)
        self.myprivileges = Privileges()
        print(self.first_name.title(), self.last_name.title(), 'is an Admin.')
